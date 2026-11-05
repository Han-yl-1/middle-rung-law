#!/usr/bin/env python3
"""Three-way BAO fit: flat LCDM, w0wa (CPL dynamical dark energy), and the Middle-Rung (coasting) model.

Usage:
    python3 fit_bao.py                      # uses desi_dr2.csv in this folder
    python3 fit_bao.py path/to/table.csv    # same columns, e.g. DESI final release

Table columns: tracer,z,kind,value,sigma,rho
  kind = V (D_V/r_d, single row) or MH (D_M/r_d in value/sigma, D_H/r_d in value2/sigma2, correlation rho)
BAO-only: each model is fitted with r_d free (absorbed in the scale parameter c/(H0 r_d)).
Pure Python (no numpy/scipy), Nelder-Mead minimizer.
"""
import csv, math, os, sys

C = 299792.458  # km/s

def load(path):
    rows = []
    for r in csv.DictReader(open(path)):
        r['z'] = float(r['z'])
        for k in ('value', 'sigma', 'value2', 'sigma2', 'rho'):
            r[k] = float(r[k]) if r.get(k) not in (None, '') else None
        rows.append(r)
    return rows

def integ(f, a, b, n=600):
    if b <= a:
        return 0.0
    u0, u1 = math.log1p(a), math.log1p(b)
    s = (u1 - u0) / n
    tot = 0.0
    for i in range(n):
        u = u0 + (i + 0.5) * s
        z = math.exp(u) - 1
        tot += f(z) * (1 + z)
    return tot * s

# --- models: return E(z) = H(z)/H0 -----------------------------------------
def E_lcdm(p):
    om = p[0]
    return lambda z: math.sqrt(om * (1 + z) ** 3 + 1 - om)

def E_w0wa(p):
    om, w0, wa = p[0], p[1], p[2]
    def E(z):
        a = 1 / (1 + z)
        de = a ** (-3 * (1 + w0 + wa)) * math.exp(-3 * wa * (1 - a))
        return math.sqrt(om * (1 + z) ** 3 + (1 - om) * de)
    return E

def E_rung(p):
    # coasting H = H0 (1+z) below z_s; matter (+radiation) above, continuous at z_s
    zs = p[0]
    wr_over_wm = 4.18e-5 / 0.143
    def E(z):
        if z <= zs:
            return 1 + z
        f = lambda x: math.sqrt((1 + x) ** 3 + wr_over_wm * (1 + x) ** 4)
        return (1 + zs) * f(z) / f(zs)
    return E

MODELS = {
    'LCDM (Om, scale)':        (E_lcdm, [0.31], [(0.05, 0.9)]),
    'w0wa (Om, w0, wa, scale)': (E_w0wa, [0.31, -0.9, -0.5], [(0.05, 0.9), (-3, 1), (-5, 3)]),
    'Middle-Rung coasting (z_s, scale)': (E_rung, [1.6], [(0.2, 6.0)]),
}

def chi2(rows, Emaker, p, scale):
    E = Emaker(p)
    t = 0.0
    cache = {}
    for r in rows:
        z = r['z']
        if z not in cache:
            dm = integ(lambda x: 1 / E(x), 0, z)
            dh = 1 / E(z)
            cache[z] = (scale * dm, scale * dh)
        DM, DH = cache[z]
        if r['kind'] == 'V':
            DV = (z * DM * DM * DH) ** (1 / 3)
            t += ((DV - r['value']) / r['sigma']) ** 2
        else:
            a = (DM - r['value']) / r['sigma']
            b = (DH - r['value2']) / r['sigma2']
            rho = r['rho']
            t += (a * a + b * b - 2 * rho * a * b) / (1 - rho * rho)
    return t

def nelder_mead(f, x0, step, iters=600):
    n = len(x0)
    pts = [list(x0)]
    for i in range(n):
        x = list(x0); x[i] += step[i]; pts.append(x)
    vals = [f(x) for x in pts]
    for _ in range(iters):
        order = sorted(range(n + 1), key=lambda i: vals[i])
        pts = [pts[i] for i in order]; vals = [vals[i] for i in order]
        cen = [sum(p[j] for p in pts[:-1]) / n for j in range(n)]
        xr = [cen[j] + (cen[j] - pts[-1][j]) for j in range(n)]; fr = f(xr)
        if fr < vals[0]:
            xe = [cen[j] + 2 * (cen[j] - pts[-1][j]) for j in range(n)]; fe = f(xe)
            pts[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = [cen[j] + 0.5 * (pts[-1][j] - cen[j]) for j in range(n)]; fc = f(xc)
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                for i in range(1, n + 1):
                    pts[i] = [pts[0][j] + 0.5 * (pts[i][j] - pts[0][j]) for j in range(n)]
                    vals[i] = f(pts[i])
    i = min(range(n + 1), key=lambda i: vals[i])
    return pts[i], vals[i]

def fit(rows, name):
    Emaker, p0, bounds = MODELS[name]
    def f(x):
        p, scale = x[:-1], x[-1]
        for v, (lo, hi) in zip(p, bounds):
            if not lo <= v <= hi:
                return 1e9
        return chi2(rows, Emaker, p, scale)
    x0 = p0 + [30.0]
    step = [0.05] * len(p0) + [1.0]
    best, val = nelder_mead(f, x0, step)
    best, val = nelder_mead(f, best, [s / 5 for s in step])
    return best, val

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'desi_dr2.csv')
    rows = load(path)
    npts = sum(1 if r['kind'] == 'V' else 2 for r in rows)
    print(f'data: {path}  ({npts} measurements)')
    for name in MODELS:
        best, val = fit(rows, name)
        k = len(best)
        aic = val + 2 * k
        pars = ', '.join(f'{v:.4f}' for v in best)
        print(f'{name:36s} chi2 = {val:7.2f}  dof = {npts - k:2d}  AIC = {aic:7.2f}  params = [{pars}]')
    print('scale = c/(H0 r_d); r_d free in all models (BAO-only).')

if __name__ == '__main__':
    main()

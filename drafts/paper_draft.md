# A coasting late universe from a three-rung frequency ladder: preregistered predictions confronted with DESI BAO

John Lu Qianhe, Zhang Xiangqian — DRAFT (fill [FINAL] slots when DESI final BAO is released)

## Abstract
We test a preregistered model (OSF 10.17605/OSF.IO/SPRZJ, fixed 2026-11-05) in which the Planck frequency is the geometric mean of the Hubble rate H and an ether frequency ν_e (ν_e H = ν_P²), with standard early-universe physics and a switch to coasting expansion, H ∝ 1+z, near z ≈ 1.6. Against DESI DR2 BAO (13 measurements, r_d free) the model gives χ² = 21.6 for 11 d.o.f. versus 10.5 for flat ΛCDM and 5.8 for w0wa. [FINAL: results with the DESI final release.]

## 1. Model
- Middle-rung law and its interpretation (Hubble-sphere de Broglie frequency; Zhang 2026 normalization relation).
- Expansion history: ΛCDM-like early phase, coasting below z_s; z_s fixed by the CMB acoustic angle (≈1.6–1.7) or fitted (BAO-only).
- Number of free parameters for BAO-only fits: z_s and c/(H0 r_d) — the same count as flat ΛCDM.

## 2. Preregistered predictions (unchanged)
P1–P5 as in the OSF record.

## 3. Data and method
- DESI DR2 BAO, Table 4 of arXiv:2503.14738 (BGS D_V/r_d; LRG, ELG, QSO, Lyα D_M/r_d and D_H/r_d with correlations).
- Pure-Python fitting code in `analysis/fit_bao.py`; validation: flat ΛCDM BAO-only gives Ω_m = 0.297, matching the DESI value (0.2975).
- [FINAL: DESI final table.]

## 4. Results (DR2)
| Model | free params | χ² | AIC |
|---|---|---|---|
| Flat ΛCDM | 2 | 10.54 | 14.54 |
| w0wa | 4 | 5.81 | 13.81 |
| Middle-rung coasting | 2 (z_s = 1.54) | 21.64 | 25.64 |
Largest residual of the coasting model: D_H at z = 0.934.
[FINAL: same table.]

## 5. Other predictions
- P5 (acceleration scale): Ciocan et al. 2026 find a₀(z≈1) = 2.38×10⁻¹⁰ m/s², direction as predicted, magnitude ~19% above.
- P1 (H₀): pending gravitational-wave standard sirens.

## 6. Discussion
- What a confirmation of P3 would and would not establish (coasting phase vs. the ether interpretation).
- Degeneracy with dynamical dark energy; parameter economy of the coasting model.
- Known tensions: local distance ladder (H₀ ≈ 70–75).

## References
DESI Collaboration 2025 (arXiv:2503.14738, 2503.14739); Planck 2020; Ciocan et al. 2026; Milgrom 1983, 2017; Melia & Shevchuk 2012; Weinberg 1972; Zhang 2026 (unpublished).

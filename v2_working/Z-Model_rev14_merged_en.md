# The Mother Equation: A Cross-Scale Spacetime Impedance Framework Based on ΔN = −1 Topological Breaking (Z-Model)

**Abstract** This paper proposes a cross-scale spacetime framework (Z-Model) that takes a normalized mother equation as its first axiom. Space is regarded as the only entity in motion: a right-handed helical fractal flow diverging outward at the speed of light, whose network carries a topological gap of 1/6 dimension (ΔN = −1, N = 6). From this we derive the effective spacetime impedance $\mathcal{Z}_{\text{eff}}(r,\nu)$ and the running effective dimension $D_{\text{eff}}(\mathcal{C})$, which share a single dimensionless control parameter $\mathcal{C}$. In the macroscopic low-frequency limit the framework reduces exactly to Keplerian-Newtonian mechanics (the gap self-concealment theorem); all new physics is concentrated in the dynamical window (delays, dispersion, scattering geometry), and concentrated near the phase-lock frequency of 17.8 eV. Within the existing axioms we derive a variable-impedance quantum wave equation, high-frequency corrected field equations, a relativistic momentum correction, and a critical phase-lock control law, and we further give sets of application equations for tunneling, transport, superconductivity, and propulsion. Attosecond photoionization delay (Route 1) is the primary test channel and is responsible for calibrating the framework's only undetermined constant $\mathcal{A}$.

## 1. The Mother Equation: An Expression That Must Equal 1

$$4\pi^2\cdot r^3\cdot (r_{\text{lock}}/r)^\delta\cdot (c^2-v^2) / ( T^2\cdot E_{\text{src}}\cdot \mathcal{Z}_{\text{eff}}(r,\nu) ) = 1$$

where:
- $\delta(\mathcal{C}) = (1/6)\cdot\mathcal{C}/(1+\mathcal{C}) \in [0, 1/6]$ — the volume-exponent deviation; for $\mathcal{C}\ll1$, $\delta\to0$ and the equation reverts to the form without fractal correction
- $D_{\text{eff}}(\mathcal{C}) = 3 - \delta(\mathcal{C})$ — the running effective dimension, moving smoothly from 3 (macroscopic) to 17/6 (fully fractal)
- $\mathcal{C}(r,\nu) = \mathcal{A}\cdot(r_{\text{lock}}/r)^{1/6}\cdot(\nu/\nu_{\text{lock}})^2$ — the fractal activation depth (dimensionless; defined in §6)

It is a modified version of Kepler's third law. The numerator $4\pi^2\cdot r^3\cdot (r_{\text{lock}}/r)^\delta$ is a running Keplerian geometry, $(c^2-v^2)$ is the special-relativistic factor, and in the denominator $E_{\text{src}}$ is the source energy and $\mathcal{Z}_{\text{eff}}$ is the effective spacetime impedance.

The whole expression is identically equal to 1. This is the first axiom: at whatever scale, large or small, the system must balance its account on this expression. Normalization itself is the entry point to this cosmology.

The source energy is two-state; this is the only interface between the microscopic and the macroscopic:

- Microscopic / quantum state: $E_{\text{src}} = h\nu$
- Macroscopic / gravitational state: $E_{\text{src}} = Mc^2$

The microscopic side hands energy to frequency through $h\nu$; the macroscopic side hands energy to mass through $Mc^2$. A single $E_{\text{src}}$ connects the quantum and gravitational ends.

### 1.1 Clause Zero: The Operational Definition of ν

**Clause.** The $\nu$ in the mother equation and in the control parameter $\mathcal{C}(r,\nu)$ is defined as **the frequency of the external driving field applied to the system**, not any intrinsic frequency of the system itself. In a dark environment (no external drive) $\nu = 0$, hence $\mathcal{C} \equiv 0$.

Note the distinction between two easily confused symbols: $v$ (Latin) is velocity, appearing in $(c^2-v^2)$ and $rv^2(1-v^2/c^2)$; $\nu$ (Greek) is frequency, appearing in $\mathcal{Z}_{\text{eff}}(r,\nu)$ and $(\nu/\nu_{\text{lock}})^2$.

**This is not a convention; it is forced by the following theorem.**

**Impossibility theorem.** Let $\nu$ be any intrinsic function of the system's own scale $r$, $\nu = K\cdot c/r^{\,p}$ ($K$ a constant, $p>0$). Substituting into the control parameter:

$$\mathcal{C}(r) = \mathcal{A}\left(\frac{r_{\text{lock}}}{r}\right)^{1/6}\left(\frac{Kc/r^{\,p}}{\nu_{\text{lock}}}\right)^{2} \;\propto\; r^{-1/6-2p}$$

For any $p>0$, $\mathcal{C}$ diverges monotonically as the scale decreases, and **is a function of $r$ only**.

But the framework simultaneously requires:

1. An atom in a dark environment has $\mathcal{C}\ll1$ — otherwise the mass rheology $M_{\text{eff}}=M_0/(1+\mathcal{C})$ would change the Rydberg constant, in conflict with the measured precision of $4.2\times10^{-15}$ for the hydrogen 1S–2S transition (see §19, Route 5);
2. The same atom under 17.8 eV extreme-ultraviolet drive has $\mathcal{C}\sim1$ — otherwise Route 1 has no signal, $\mathcal{A}$ is suppressed to nothing, and §21–24 are all eliminated.

If $\mathcal{C}=\mathcal{C}(r)$, a given atom can have only one value of $\mathcal{C}$, and the two requirements cannot both be satisfied. **Therefore $\nu$ must be a free variable, decoupled from the system's scale and externally tunable.**∎

**Corollary (disposition of the topological reading).** A natural geometric conjecture is: each turn of the spatial helix closes only $300°$, falling short by $60°$, so the phase slip rate of the gap is $\nu_{\text{gap}}(r)=\frac{1}{6}\cdot\frac{c}{r}$. Substituting gives

$$\mathcal{C} = \frac{\mathcal{A}}{36}\left(\frac{r_{\text{lock}}}{r}\right)^{1/6+2} = \frac{\mathcal{A}}{36}\left(\frac{r_{\text{lock}}}{r}\right)^{13/6}$$

The exponent falls automatically on $13/6$ — precisely the signature exponent of the impedance branch in §17, which is algebraically quite striking. But this is the case $p=1$, which is excluded by the theorem above: at the atom, $\nu=\frac{1}{6}(c/a_0)\approx3905$ eV, $\mathcal{C}/\mathcal{A}\approx1.6\times10^{5}$, and hydrogen spectroscopy gives $\mathcal{A}<6\times10^{-18}$.

**What the topology actually governs is $\nu_{\text{lock}}$, not $\nu$.** The mother equation already contains two frequencies: $\nu_{\text{lock}}$ is the framework's own phase-lock frequency, given by topology, and $\nu$ is the externally supplied driving frequency; physical effects depend only on their ratio. The intuition that "there is a frequency on each side of the gap" is already embodied in the structure of $(\nu/\nu_{\text{lock}})^2$. The remaining open point is that $\nu_{\text{lock}}$ is at present still an input rather than a derived quantity (see the note in §10).

**Cost (must be stated together with the clause).** Once this clause is adopted, the framework's predictions for all **static** properties — mass, fundamental constants, ground-state structure, zero-field spectroscopy — are uniformly zero. All new physics occurs only under external drive, i.e., Routes 1, 3, and 4. This is the price the framework pays for its survival, and it must be stated explicitly.

## 2. The Motion of Space: Right-Handed Helical Divergence at the Speed of Light

Space is not a static background; it is the only entity in motion.

The space around an object is, at every moment, moving outward in a helical divergence at the speed of light. The direction is described by a right-hand analogy: extend the right hand, take the thumb as the axis, and let the four fingers unfold counterclockwise — space diverges outward ceaselessly at the speed of light in such a right-handed helix.

This perpetual right-handed light-speed helix is the source of every structure that follows: its rotational kinetic energy gives the frequency-squared law $\beta = 2$, its process of weaving a network outward unfolds as time, and the gap it leaves by not weaving the network completely gives the 1/6 dimension. All things are standing waves and knots that this helix catches at different frequencies and different scales.

(Lineage note: this kinematic foundation shares its origin with the basic postulate of Mr. Zhang Xiangqian's unified field theory; the Z-Model's only axiom-level modification of it is one point — this helical network is not completely woven, lacking 1/6 dimension. See *The Mother Equation × Mr. Zhang Xiangqian's Unified Field Theory: Comparison and New Derivations*.)

## 3. 𝒵₀: The Baseline Impedance of Spacetime

$\mathcal{Z}_0$ is the baseline impedance of spacetime in the absence of topological breaking; it is the underlying stiffness by which space maintains its normalized balance. When topological breaking is zero and the correction term vanishes, the system is left with only this basic coupling strength.

The physical analogy is the vacuum impedance of electromagnetism, $\sqrt{\mu_0/\varepsilon_0} \approx 377\ \Omega$ — but the analogy holds only at the level of "the basic impedance of space to some kind of flow": the dimension of $\mathcal{Z}_0$ is $L^3M^{-1}T^{-2}$ (that is, the dimension of G, not ohms), and numerically it is not equal to $377\ \Omega$. What is resisted here is not electromagnetic waves but curvature, waves, and orbital motion; in the macroscopic gravitational limit, $\mathcal{Z}_0$ is calibrated to G.

Notational conventions: baseline impedance $\mathcal{Z}_0$; **defect-core scale** $r_{\text{core}} \approx l_p$, $\nu_{\text{core}} = c/r_{\text{core}} \approx \nu_p$ (Planck cutoff, governing the soliton body); **phase-lock scale**, generated by a single input quantity, the **phase-lock period** $T_{\text{lock}}$.

**The geometric identity of the phase-lock scale: the helix pitch.** $r_{\text{lock}}$ is not an independent length input; it is the **helix pitch** of the light-speed helix — the distance the helix advances along its axis for each completed phase-lock period:

$$r_{\text{lock}} \equiv c\,T_{\text{lock}}\,,\qquad \nu_{\text{lock}} \equiv 1/T_{\text{lock}} = c/r_{\text{lock}}\,,\qquad E_{\text{lock}} \equiv h/T_{\text{lock}}$$

Taking $T_{\text{lock}} = 232$ as (for its source, see the calibration statement in §10):

| Quantity | Expression | Value |
|---|---|---|
| Phase-lock period | $T_{\text{lock}}$ | 232 as |
| Helix pitch | $c\,T_{\text{lock}}$ | 69.55 nm |
| Phase-lock frequency | $1/T_{\text{lock}}$ | $4.310\times10^{15}$ Hz |
| Angular frequency | $2\pi/T_{\text{lock}}$ | $2.708\times10^{16}$ rad/s |
| Phase-lock energy | $h/T_{\text{lock}}$ | 17.83 eV |

This explains the relation $\nu_{\text{lock}} = c/r_{\text{lock}}$, previously given as a "convention": it is not a convention but an **identity** of helical geometry — pitch divided by period is always the speed of light. The two scales (defect core / phase-lock) are each internally locked by $\nu = c/r$ and do not cross-talk.

## 4. Dimensions: It Is the Dimension of the Gravitational Constant

Dimensional analysis of the mother equation: the numerator $r^3(c^2-v^2)$ gives $L^5T^{-2}$, which becomes $L^5T^{-4}$ with $4\pi^2/T^2$; the denominator is energy $ML^2T^{-2}$ times $[\mathcal{Z}_0]$. For the left side to be dimensionless:

$$[\mathcal{Z}_0] = L^3M^{-1}T^{-2}$$

This is exactly the dimension of Newton's gravitational constant G. In the macroscopic classical limit, $\mathcal{Z}_0$ is calibrated to G. The baseline stiffness of spacetime and the constant that sustains universal gravitation are the same thing under the same dimension.

After the numerator $r^3$ is rewritten as $r^{D_{\text{eff}}} \equiv r^3\cdot(r_{\text{lock}}/r)^\delta$, $(r_{\text{lock}}/r)^\delta$ is a dimensionless factor ($\delta\in[0,1/6]$, $r_{\text{lock}}/r$ being a ratio of lengths), the numerator as a whole still has dimension $L^3$, and $[\mathcal{Z}_0] = L^3M^{-1}T^{-2}$ needs no adjustment. Here $r_{\text{lock}}$ plays two roles at once: ① the phase-lock manifestation scale (governing the experimental window, see §3); ② the dimensional anchor (making the fractional power dimensionally consistent in the equation). The two roles share one numerical value, $r_{\text{lock}} \approx 69.6\text{ nm}$; this is intentional, and no additional parameter is introduced.

## 5. The Direction of the Frequency Term: The More Microscopic, the More the Wound of Space Shows

Effective spacetime impedance:

$$\mathcal{Z}_{\text{eff}}(r,\nu) = \mathcal{Z}_0\cdot\left[ 1 + \mathcal{A}\cdot(r_{\text{lock}}/r)^{1/6}\cdot(\nu/\nu_{\text{lock}})^2 \right]$$

where $\mathcal{A}$ is a dimensionless coupling constant of order $\mathcal{O}(1)$, calibrated by experiment. The theory fixes the shape of the correction term — scale power 1/6 and frequency power 2; its absolute amplitude $\mathcal{A}$ is left for attosecond / nanometer experiments to test.

The frequency term is $(\nu/\nu_{\text{lock}})^2$, oriented toward high frequency: at large scales ($r \gg r_{\text{lock}}$) the correction is weak, at low frequency ($\nu \ll \nu_{\text{lock}}$) the correction is weak, and only small scale combined with high frequency makes it manifest. This matches the nature of space — the higher the frequency, the more microscopic, the shorter the scale, the more visible the scar of that gap.

(If the frequency term were written in reverse as $(\nu_{\text{lock}}/\nu)^2$, oriented toward low frequency, the correction term for macroscopic orbits would blow up to order $10^{94}$. Orientation toward high frequency is the only choice that makes the microscopic forbidden zone manifest while keeping the macroscopic regime stable.)

## 6. Control Parameter and Classical Limit: Exact Reduction to Kepler

Dimensionless control parameter:

$$\mathcal{C}(r,\nu) = \mathcal{A}\cdot(r_{\text{lock}}/r)^{1/6}\cdot(\nu/\nu_{\text{lock}})^2$$

- $\mathcal{C} \ll 1$: classical regime
- $\mathcal{C} \sim 1$: transition regime; the topological wound begins to be significant
- $\mathcal{C} \gg 1$: wound-manifest regime; quantum defects dominate

In the classical regime ($\mathcal{C} \ll 1$), $\mathcal{Z}_{\text{eff}} \approx \mathcal{Z}_0$; taking the macroscopic mode $E_{\text{src}} = Mc^2$, $\mathcal{Z}_0 = G$, the mother equation becomes $4\pi^2r^3(c^2-v^2) / (T^2\cdot Mc^2\cdot G) = 1$, which at low speed reduces exactly to:

$$4\pi^2r^3 / T^2 = GM$$

Taking the Earth's orbit around the Sun as an example to verify the macroscopic safety of the single-term form: orbital frequency $\nu_{\text{orbit}} \approx 3.17\times10^{-8}\text{ Hz}$, frequency term $(\nu_{\text{orbit}}/\nu_{\text{lock}})^2 \approx 5.4\times10^{-47}$, geometric term $(r_{\text{lock}}/r)^{1/6} \approx 8.8\times10^{-4}$, giving the product $\mathcal{C} \approx 4.8\times10^{-50} \ll 1$. What actually suppresses the macroscopic correction is the frequency-squared term; the single-term form need not be split into two scales, and macroscopic safety is guaranteed by the frequency term alone.

When $\mathcal{C} \ll 1$, $\delta = (1/6)\cdot\mathcal{C}/(1+\mathcal{C})\to0$, the numerator $r^3\cdot(r_{\text{lock}}/r)^\delta\to r^3$, and the mother equation reduces exactly to the form without fractal correction. The Earth–Sun estimate above simultaneously guarantees $\delta \approx 0$, so Keplerian safety is not affected in any way.

## 7. μ-Degeneracy and the Local Form: The Mother Equation Recognizes Only the Product m𝒵

Using $v = 2\pi r/T$ on the macroscopic branch to eliminate the period T, the mother equation is rearranged into a local form that does not contain T:

$$m\cdot\mathcal{Z}_{\text{eff}}(r,\nu) = r\cdot v^2\cdot(1 - v^2/c^2)$$

The right side is a purely geometric-kinematic quantity. This expression says something deep: **in the gravitational regime, the only observable has always been the product m𝒵; the split between mass and impedance is a convention**. This is not a novelty of this model but an established fact of mainstream celestial mechanics — orbital measurements directly give the gravitational parameter $\mu = GM$ (the Earth's GM has been measured to ten significant figures), whereas G and M individually are known only to five: because from orbits alone, G and M simply cannot be separated. The mother equation elevates this fact, long taken for granted in the mainstream, to a structural principle: **μ-degeneracy**.

The meeting of the two limiting ends: as $v \to 0$ it reduces to Kepler; as $v \to c$ the left side tends to zero — mass dissolves in the light-speed limit, interlocking in the same limit with the photon picture that "a massless entity must move at the speed of light". The mother equation closes at both ends.

## 8. The Geometric Origin of α = 1/6: r^(D_eff) Is a Running Volume Verdict

$r^{D_{\text{eff}}}$ is a running volume verdict. Space is a fractal network woven by the right-handed light-speed helix, and the true exponent of volume growth is not a fixed 3 but an effective dimension $D_{\text{eff}}$ that runs with the activation depth $\mathcal{C}$:

$$D_{\text{eff}}(\mathcal{C}) = 3 - (1/6)\cdot\mathcal{C}/(1+\mathcal{C})$$

At macroscopic scales $\mathcal{C} \ll 1$, $D_{\text{eff}} \to 3$, and the verdict is "three-dimensional Euclidean space, Kepler holds"; at microscopic high frequency $\mathcal{C} \gg 1$, $D_{\text{eff}} \to 17/6$, and the verdict is "the helical fractal is fully unfolded, volume is computed as $r^{17/6}$". In the transition regime ($\mathcal{C} \sim 1$) there is a smooth transition between the two, steered by the same control parameter $\mathcal{C}$.

$\alpha = 1/6$ is not a fixed correction constant but the asymptotic upper limit of the deviation of $D_{\text{eff}}$ from three dimensions: as $\mathcal{C} \to \infty$, $D_{\text{eff}}$ descends at most to 17/6 and can go no lower — the topological constraint of six-fold symmetry gives this lower bound.

The frequency exponent $\beta = 2$ originates from the same helix: gravity is the reverse manifestation of the rotational kinetic energy of the flow, $G_{\text{eff}} \propto 1/E_{\text{rot}}$, $E_{\text{rot}} \propto \nu^2$, hence $\beta = 2$. $\alpha$ and $\beta$ are two bones grown from the same $D = 17/6$ helical fractal network; only $\alpha$ runs, because it carries the gating of $\mathcal{C}$.

## 9. Necessarily 1/6, Necessarily Six-Fold

For N-fold symmetry, the topological gap is apportioned as: $\alpha = |\Delta N|/N$, $D = 3 - |\Delta N|/N$. Taking $\Delta N = -1, N = 6$: $\alpha = 1/6$, $D = 17/6$. Four hard constraints (dimensionlessness, minimal stable symmetry number, reduction to Kepler, smoothness of the orbital equation) lock it in simultaneously.

**Lineage note: a recorded failed derivation.** An attempt was made to derive $D = 17/6$ by a purely geometric route: construct a six-fold chiral hyperbolic discrete group $\Gamma_6^\chi$ and test whether the Patterson–Sullivan critical exponent of its limit set satisfies $\delta(\Gamma_6^\chi) = 17/6$. Both the numerical and the algebraic conclusions are **negative**:

- The generators preserve the decomposition $\mathbb{R}^{4,1} = \mathbb{R}^{2,1}\oplus\mathbb{R}^2$, so the group is in fact a subgroup of $SO(2,1)\times SO(2)$, and if discrete then $\delta \le 1 < 17/6$;
- The chiral twist acts on the rotation plane orthogonal to $x_0$, does not affect the growth of hyperbolic distance, and has no effect on the critical exponent;
- In a drift-method scan with word length $L\le7$ (about $2.3\times10^7$ words), $\delta$ varies continuously with step size; there is no plateau at $n=6$ and no spontaneous phase-lock solution.

**This route has been ruled out.** Therefore, in this paper the status of $\Delta N=-1$, $N=6$ is that of an **axiomatic input**, not a group-theoretic derived result. The "four hard constraints" cited in the main text (dimensionlessness, minimal stable symmetry number, reduction to Kepler, smoothness of the orbital equation) are a **self-consistency filter**, not a uniqueness proof. This is stated as it is, without downplaying.

Here $D = 17/6$ is the asymptotic upper limit of the effective dimension $D_{\text{eff}}(\mathcal{C})$ as the activation parameter $\mathcal{C}\to\infty$, not a spatial constant at arbitrary scales. What the N = 6 symmetry constraint locks is exactly this limiting value: $\Delta N = -1, N = 6 \to \alpha = 1/6 \to D_{\text{upper}} = 17/6$. At macroscopic scales $\mathcal{C}\ll1$, $D_{\text{eff}}\to3$ and Kepler holds exactly; if $D = 17/6$ were treated as a fixed constant, the macroscopic reduction could not be explained.

## 10. Helical Fractal Spacetime · Parameter Table

| Parameter | Value / expression | Meaning |
|---|---|---|
| $\alpha$ | 1/6 ≈ 0.1667 | Dimension-deficit exponent (asymptotic upper limit of the deviation of $D_{\text{eff}}$ from three dimensions) |
| $\beta$ | 2 | Frequency power (correction term of $\mathcal{Z}_{\text{eff}}$) |
| $D$ | 17/6 ≈ 2.8333 | Helical fractal dimension (asymptotic limit of $D_{\text{eff}}$ as $\mathcal{C}\to\infty$) |
| $D_{\text{eff}}(\mathcal{C})$ | $3 - (1/6)\cdot\mathcal{C}/(1+\mathcal{C})$ | Running effective dimension, $\mathcal{C}\ll1\to3$, $\mathcal{C}\gg1\to17/6$ |
| $\delta(\mathcal{C})$ | $(1/6)\cdot\mathcal{C}/(1+\mathcal{C}) \in [0, 1/6]$ | Volume-exponent deviation; $\delta=0$ macroscopic, $\delta=1/6$ fully fractal |
| Deficit angle | 60° | Dimensional gap expressed as a circular angle |
| Effective closure angle | 300° | 360° − 60° |
| Phase-lock period | 232 as | Corresponds to $\nu_{\text{lock}}$ |
| $T_{\text{lock}}$ | = 232 as | **Phase-lock period (the only scale input, taken from a numerical calculation; see §10.1)** |
| $r_{\text{lock}}$ | $= cT_{\text{lock}}$ ≈ 69.55 nm | Helix pitch (converted from $T_{\text{lock}}$; not an independent parameter) |
| $\nu_{\text{lock}}$ | $= 1/T_{\text{lock}}$ ≈ 4.310×10¹⁵ Hz ↔ 17.83 eV | Phase-lock frequency (converted quantity) |
| $r_{\text{core}}$ | = l_p | Defect-core scale (Planck cutoff) |
| $\nu_{\text{core}}$ | = ν_p | Defect-core frequency |

**Parameter count.** The framework has **two** free inputs: the dimensionless coupling constant $\mathcal{A}$, and the **phase-lock period** $T_{\text{lock}}$. The $r_{\text{lock}}$, $\nu_{\text{lock}}$, angular frequency, and phase-lock energy in the table are **all conversions of $T_{\text{lock}}$** (see §3), not independent parameters. Several places in the earlier text referred to "the only undetermined constant $\mathcal{A}$" without counting $T_{\text{lock}}$; this is hereby corrected.

### 10.1 Calibration Statement: The Source of $T_{\text{lock}}$

$T_{\text{lock}} = 232$ as **is taken from a published numerical calculation; it is not derived by this framework, nor is it an experimental measurement**.

**Source.** W. Jiang et al., *Time Delays as Attosecond Probe of Interelectronic Coherence and Entanglement*, Phys. Rev. Lett. **133**, 163201. A collaboration between TU Wien (Burgdörfer group) and a Chinese research team, 2024. The paper performs a numerical calculation of the photoionization of the helium atom using the full-dimensional time-dependent Schrödinger equation and **computes** that the **average** time difference of the departing electron's "birth time" relative to the energy state of the remaining electron is about 232 as. This is a theoretically computed value, not an experimental measurement; whether it can be measured directly in attosecond experiments awaits future experiments.

**Three limitations that must be stated together with it:**

1. **It is an average, not a constant.** The original wording is "on average around 232 attoseconds", and it depends on the specific atom and laser configuration. This framework elevates it to a cross-scale fundamental scale; **this step itself requires independent justification, which has not yet been given**.
2. **It is not "a fixed delay constant for the establishment of entanglement".** That description is not accepted in the field and must not be used when citing it.
3. **Substitution ≠ derivation.** Knowing 232 as first and then computing $r_{\text{lock}} = cT_{\text{lock}} \approx 69.6$ nm is a **posterior interpretation**: the model assigns a geometric meaning (the helix pitch) to an already known number, but does not predict it. A genuine derivation would be: without inputting 232 as, compute $T_{\text{lock}} \approx 232$ as from other measurable quantities. **The framework cannot do this at present.**

**Consequently, 17.83 eV / 69.6 nm / $4.31\times10^{15}$ Hz are not predictions of this framework but four converted expressions of the same external input (a numerically computed value).** What is genuinely predictive in Route 1 of §17 is the **power-law shape** of the residual rising with $(\nu/\nu_{\text{lock}})^2$, not the **position** of the window (see the layered explanation in §17).

**Incidental correction.** Earlier derivation material claimed that "69.6 nm happens to be the typical scale of coherent wave packets of strong-field ionization electrons". This claim does not hold: the de Broglie wavelength of the outgoing electron in 17.8 eV photoionization is about 0.6 nm, and about 0.3 nm at 30 eV, two orders of magnitude smaller than 69.6 nm. That assertion has been deleted. Note also: a time constant of a few hundred attoseconds necessarily converts to 10–40 eV; that $T_{\text{lock}}$ corresponds to 17.8 eV, falling in the EUV window, is a necessity of dimensional conversion and does not constitute additional evidence.

### 10.2 Argument for Non-Derivability

Is it possible, without inputting 232 as, to derive a time constant of this order from within the framework? **No, and this is a structural conclusion, not a failure of search.**

**(a) Not constructible within the strict axiom set.** The only dimensional quantities the framework carries are $c$, $\hbar$, $G$ (the dimension of $\mathcal{Z}_0$ being that of $G$); the only time that can be constructed is the Planck time $t_p=\sqrt{\hbar G/c^5}=5.391\times10^{-44}$ s. The required factor

$$F=\frac{T_{\text{lock}}}{t_p}=4.303\times10^{27}$$

is not an integer power of any pure number of the framework: $\log_6 F=35.51$, $\log_{17/6}F=61.10$, $\log_{2\pi}F=34.62$, none of which is an integer.

**(b) Exhaustive-search results are swamped by noise.** Using the framework's pure numbers $\{6,\,1/6,\,17/6,\,5/6,\,\pi,\,2,\,3\}$, 2043 dimensionless combinations with total complexity $\le4$ were constructed and searched for $\pm1\%$ hits against several reference times (Rydberg period, atomic unit of time, helium correlation-energy gap), yielding 2–6 hits with a best deviation of 0.09%. But the baseline of the same search space against 2000 random targets is: **an average of 4.49 hits, with 89.0% of random targets receiving at least 1 hit**. The number of hits on the real targets is not above the noise baseline; **all are void**.

**(c) Structural prohibition (decisive).** $T_{\text{lock}}$ is taken from a full-dimensional time-dependent Schrödinger equation solution for the helium atom in a strong EUV field. Every energy scale of helium is generated by $E_h=\alpha_{\text{em}}^2 m_ec^2$; the atomic unit of time is $\hbar/E_h=24.19$ as, and $T_{\text{lock}}=9.59$ atomic time units — entirely the typical order of atomic dynamics. Yet the decoupling clause of §20 explicitly excludes $\alpha_{\text{em}}$ from the framework.

> **The framework's only external anchor lies in the region the framework itself declares it has no right to enter.**

**(d) Three ways out and the choice of this paper.**

| Way out | Content | Cost | Adopted |
|---|---|---|---|
| A | Revoke the decoupling clause of §20 | Immediately runs back into an $\alpha_{\text{em}}$ drift of about 108% ($\mathcal{A}=1$), excluded by XUV spectroscopy; $\mathcal{A}$ is suppressed to nothing, and §21–24 are all eliminated | No |
| B | Accept $T_{\text{lock}}$ as a permanent external input | The framework is permanently two-parameter ($\mathcal{A}$ and $T_{\text{lock}}$); the free parameters cannot be reduced to one | **Yes** |
| C | Switch to an anchor from a non-electromagnetic domain | Nature has no non-electromagnetic constant near $10^{-16}$ s (nuclear processes $\sim10^{-21}$ s, weak interaction $\sim10^{-6}$ s); this route is empty | No |

**This paper formally adopts way out B.** Accordingly, the positioning of §18 is updated.

## 11. The 60° Gap: The Geometric Projection of Nature's Totems

Space lacks 1/6 dimension; restored to a circular angle, this is 60°. Snowflakes, graphene, honeycombs, benzene rings, hexagonal lattices — all six-fold symmetry at the macroscopic level is the geometric shadow cast into the three-dimensional world by that underlying 60° fractal gap. Nature's geometric growth always unconsciously conforms to the skeleton of the underlying space; the ubiquity of six-fold lattices is the most direct macroscopic self-account of the topological gap of space.

## 12. Soliton Stability Radius and Lagrangian

Matter is not a substance but a knot of the motion of space. Treating the effective spacetime impedance as the coupling potential of a scalar field, we introduce the self-interaction of the scalar field $\phi$:

$$V(\phi,r) = \frac{1}{2}\,\xi(\mathcal{C})\,\mu_\phi^2\,\phi^2 + \frac{\lambda}{4}(\phi^2-\phi_0^2)^2\,,\qquad \xi(\mathcal{C}) \equiv 1+\mathcal{C}$$

where $\xi(\mathcal{C}) = 1+\mathcal{C} = \mathcal{Z}_{\text{eff}}/\mathcal{Z}_0$ is the **dimensionless** impedance rheology factor, $\mu_\phi$ is the mass parameter, $\lambda$ is the standard dimensionless quartic coupling, and $\phi_0$ is the vacuum expectation value.

(Note: the earlier formulation used the dimensional $\mathcal{Z}_{\text{eff}}$ directly as the coefficient of the quadratic term, which was dimensionally unequal to the $(\lambda/4)$ term, and the vacuum expectation value reused the symbol $v$, conflicting with the velocity $v$ of §1/§7. It is now replaced by the dimensionless $\xi(\mathcal{C})$, which carries all of the $\mathcal{C}$ dependence, and the vacuum expectation value is renamed $\phi_0$. In this way the non-minimal coupling connects directly with the $\mathcal{C}$-gating mechanism used throughout the paper, and this section no longer needs implicit geometrized units.)

Substituting the specific form of $\mathcal{Z}_{\text{eff}}$ and finding the minimum yields the soliton stability radius of the defect phase-lock (the core scale):

$$r_{\text{core}} \approx l_p\cdot\left(\frac{\hbar c^5}{\mathcal{Z}_0\,E_{\text{defect}}^{\,2}}\right)^{1/6} = l_p\cdot\left(\frac{m_P}{M_{\text{defect}}}\right)^{1/3},\qquad m_P=\sqrt{\hbar c/G}$$

(Note: in the earlier formulation, the bracket $\hbar c^3/(\mathcal{Z}_0E_{\text{defect}})$ had the dimension of **mass** rather than being dimensionless — because $\hbar c^3/(GMc^2)=\hbar c/(GM)=m_P^2/M$. Squaring the energy in the denominator and pairing it with $c^5$ makes the bracket $(m_P/M_{\text{defect}})^2$, closing the dimensions, while the exponent 1/6 is retained in the expression.)

The rest mass of matter is, in essence, the rotational kinetic energy of the spatial flow captured when this helix phase-locks at the gap and condenses into a stable soliton. The complete manifold Lagrangian is written as:

$$\mathcal{L} = \frac{1}{2}\partial_\mu\phi\,\partial^\mu\phi - V(\phi) - \frac{1}{2}\,\xi(\mathcal{C})\,R\,\phi^2\,,\qquad \xi(\mathcal{C}) = 1+\mathcal{C}$$

The non-minimal coupling term is now in the standard form $\frac{1}{2}\xi R\phi^2$, with $\xi$ dimensionless — except that in this framework it is not a constant but a running quantity gated by the control parameter $\mathcal{C}$. **The coupling strength between curvature and the scalar field is directly modulated by the activation depth of the gap**; this is the physical reading that emerges once $\mathcal{Z}_{\text{eff}}$ is replaced by $\xi$.

## 13. Coupling with Other Fundamental Equations (Derived Formula Set)

This section gives the technical implementation of cross-injecting the Z-Model mother equation into the fundamental equations of classical physics and quantum mechanics. The core mechanism is to substitute the "effective spacetime impedance $\mathcal{Z}_{\text{eff}}(r,\nu)$" and the "electron effective-mass flow $M_{\text{eff}} = M_0/(1+\mathcal{C})$" into the field equations and wave equations as topological operators.

### 13.1 Variable-Impedance Quantum Wave Equations

In the microscopic high-frequency limit, the electron effective-mass flow derived in §21 directly rewrites the relativistic **Dirac equation** for spin-1/2 particles:

$$\left( i\hbar \gamma^\mu \partial_\mu - \frac{m_0 c}{1 + \mathcal{A} \left(\frac{r_{\text{lock}}}{r}\right)^{1/6} \left(\frac{\nu}{\nu_{\text{lock}}}\right)^2} \right) \psi = 0$$

In the non-relativistic limit, the mass-flow term inversely amplifies the coefficient of the kinetic term, giving the **fractal-gated Schrödinger equation**:

$$- \frac{\hbar^2 \left[1 + \mathcal{A} \left(\frac{r_{\text{lock}}}{r}\right)^{1/6} \left(\frac{\nu}{\nu_{\text{lock}}}\right)^2\right]}{2m_0} \nabla^2 \psi + V\psi = i\hbar \partial_t \psi$$

**Physical effect:** When matter is placed in an extreme-ultraviolet high-frequency environment close to $\nu_{\text{lock}}$ (17.8 eV), the local control parameter $\mathcal{C}$ rises sharply and the mass operator weakens. This not only gives an underlying explanation for the change in electron wave-packet group velocity and dispersion (the cause of the delay in the Route 1 experiment), but also predicts that within the phase-lock window the barrier-penetration probability of particles (quantum tunneling) will rise nonlinearly and exponentially (for the quantitative form see §24.1).

### 13.2 High-Frequency-Corrected Einstein Field Equations

In general relativity, the Einstein gravitational constant $\kappa = 8\pi G / c^4$ rests on the baseline spacetime impedance $\mathcal{Z}_0$. Replacing it with the running impedance $\mathcal{Z}_{\text{eff}}(r,\nu)$ gives the high-frequency-corrected gravitational field equations:

$$R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} = \frac{8\pi \mathcal{Z}_0 \left[ 1 + \mathcal{A}\left(\frac{r_{\text{lock}}}{r}\right)^{1/6}\left(\frac{\nu}{\nu_{\text{lock}}}\right)^2 \right]}{c^4} T_{\mu\nu}$$

**Physical effect:** Under conditions of high astrophysical energy density combined with high frequency (e.g., standing waves from neutron-star collisions, artificial high-frequency modulated flows), the local spacetime stiffness increases substantially, and an energy-momentum tensor $T_{\mu\nu}$ of the same strength will excite spacetime distortion far exceeding conventional predictions. This provides field-equation-level theoretical support for macroscopic anti-gravity technology and the propulsion extension.

### 13.3 Running Fractal Laplacian

Because the effective dimension $D_{\text{eff}}(\mathcal{C})$ runs with the activation depth, the conventional Euclidean three-dimensional Laplacian requires a manifold-homeomorphism correction in dynamics. We define the **running fractal Laplacian**:

$$\nabla^2_{D_{\text{eff}}} \Phi = \frac{1}{r^{D_{\text{eff}}(\mathcal{C})-1}} \partial_r \left( r^{D_{\text{eff}}(\mathcal{C})-1} \partial_r \Phi \right) + \Omega_{\text{angular}}$$

where the effective dimension is $D_{\text{eff}}(\mathcal{C}) = 3 - \frac{1}{6}\frac{\mathcal{C}}{1+\mathcal{C}}$. This equation quantitatively constrains the non-Euclidean geometric behavior of wave dispersion and small-angle scattering in the transition region ($\mathcal{C} \sim 1$), and meshes precisely with Route 3 of §17 (the EUV scattering-fingerprint experiment).

## 14. Lorentz–Impedance Relativistic Extension and Light-Speed Flight Control

This section carries the impedance flow of the mother equation further into relativistic kinematics and dynamics, derives higher-order derived equations, and rigorously balances, in mathematical terms, the control conditions for "a macroscopic object with rest mass crossing the speed of light."

### 14.1 Lorentz–Impedance Cooperative Momentum Equation

Starting from the classical special-relativistic momentum $p = \gamma m v$ and incorporating the dissolution of intrinsic inertia brought by the impedance flow of the mother equation, we derive a new momentum formula that includes the field excitation frequency:

$$p = \frac{\gamma M_0 v}{1 + \mathcal{C}} = \frac{M_0 v}{\sqrt{1 - \frac{v^2}{c^2}} \cdot \left[ 1 + \mathcal{A}\left(\frac{r_{\text{lock}}}{r}\right)^{1/6}\left(\frac{\nu}{\nu_{\text{lock}}}\right)^2 \right]}$$

**Physical effect:** This formula breaks the conventional rule that momentum is determined one-directionally by velocity alone. It indicates that by applying an external high-frequency impedance of a specific frequency in local space ($\mathcal{C} \gg 1$), the Lorentz inertial inflation of an object can be offset in the reverse direction from the motion.

### 14.2 High-Frequency-Corrected Geodesic Flow Equation

Combined with the high-frequency-corrected field equations, when a massive object moves in an artificially controlled field manifold containing an impedance gradient, its classical geodesic free-fall trajectory is shifted. The corresponding flow equation for the connection operator (Christoffel symbols) is:

$$\Gamma^\mu_{\alpha\beta}(\mathcal{C}) = \Gamma^\mu_{\alpha\beta} + \frac{1}{2}\left( \delta^\mu_\alpha \partial_\beta \ln(1+\mathcal{C}) + \delta^\mu_\beta \partial_\alpha \ln(1+\mathcal{C}) - g_{\alpha\beta}\partial^\mu \ln(1+\mathcal{C}) \right)$$

**Physical effect:** This is an "artificial gravity / spacetime-curvature control" equation that requires no conventional reaction mass. As long as an asymmetric impedance gradient $\partial\ln(1+\mathcal{C})$ of the spatial control parameter $\mathcal{C}$ is created around the spacecraft, the object will acquire an autonomous acceleration along the new geometric-topological geodesic (for the weak-field quantitative form see §24.4).

### 14.3 Running-Dimension Path-Integral Propagator

The Feynman path-integral propagator describing the evolution of high-frequency microscopic wave packets on a variable-dimension manifold is modified to:

$$K(x_f, t_f; x_i, t_i) = \int \mathcal{D}[x(t)] \exp\left( \frac{i}{\hbar} \int \left[ \frac{1}{2}M_0 (1+\mathcal{C})^{-1} \left(\frac{dx}{dt}\right)^2 - V(x) \right] dt \right)$$

(Note: an earlier version wrote $d^{D_{\text{eff}}(\mathcal{C})}t$. Dimensional recheck: the bracket has dimensions of energy $ML^2T^{-2}$; after multiplying by $T^{D_{\text{eff}}}$ and dividing by $\hbar$, a residual $T^{D_{\text{eff}}-1}$ remains, which is dimensionless only when $D_{\text{eff}}=1$, whereas $D_{\text{eff}}\approx 2.83$. Time is one-dimensional; the running dimension belongs to the **path measure** $\mathcal{D}[x]$, not to the time integral. Hence the measure is changed back to $dt$, and the definition of the fractal structure is moved into $\mathcal{D}[x]$.

If a fractional time measure must be retained, the only dimensionally closed form is to introduce the phase-lock period as a regularization: $\tau_{\text{lock}}^{\,1-D_{\text{eff}}}(dt)^{D_{\text{eff}}}$, where $\tau_{\text{lock}}=1/\nu_{\text{lock}}=232\text{ as}$ — no new parameter is introduced.)

This formula provides the mathematical foundation, on a full fractal grid, for quantitatively computing higher-order electron wave-packet dispersion in attosecond experiments (the Route 1 channel).

### 14.4 Critical Phase-Lock Control Equation (Balancing Light-Speed Flight)

Under the variable-impedance kinetic-energy mechanism, the relativistic kinetic-energy equation of a massive spacecraft in motion is rewritten as:

$$E_k(\mathcal{C}, v) = \frac{\gamma - 1}{1+\mathcal{C}} M_0 c^2$$

In conventional relativity, as the spacecraft's speed approaches the speed of light ($v \to c$), the Lorentz factor $\gamma \to \infty$ and the kinetic-energy requirement diverges.

**Cooperative phase-lock control condition:** Let the activation depth $\mathcal{C}$ output by the spacecraft's high-frequency generator dynamically track and phase-lock to the increase in the spacecraft's speed (the growth of $\gamma$), so that it strictly satisfies the linear control law:

$$1 + \mathcal{C} = k \cdot \gamma \quad (\text{where } k \ge 1 \text{ is an artificial control coefficient})$$

Then, taking the limit of the kinetic-energy expenditure as the spacecraft approaches the light-speed limit indefinitely:

$$\lim_{v \to c} E_k = \lim_{\gamma \to \infty} \frac{\gamma - 1}{k \cdot \gamma} M_0 c^2 = \frac{1}{k} M_0 c^2$$

**Astronautical verdict:** As $v \to c$, the nonlinear enhancement of spacetime impedance (geometric dissolution of mass) **offsets with extreme precision the explosion of Lorentz inertial mass brought about by velocity**. The energy required for the spacecraft to approach the speed of light indefinitely is no longer infinite, but converges to an absolutely finite fixed value $\frac{1}{k}M_0 c^2$ (for $k=1$, this is the spacecraft's rest energy). At the light-speed threshold, the spacecraft's effective inertia is completely dissolved, and on the manifold it is converted as a whole into a **macroscopic standing-wave coherent soliton** held in place by the right-handed helical spatial flow (i.e., a macroscopic photon picture), achieving interstellar light-speed travel.

## 15. Macroscopic High-Frequency Phase-Lock Field Control Equations

To extend the microscopic effective-impedance transition in the mother equation to the exterior of a macroscopic spacecraft, a macroscopic quantum coherent amplification mechanism must be introduced to overcome geometric attenuation at large scales.

**15.1 Macroscopic coherent activation equation:**

$$\mathcal{C}_{\text{macro}} = N_c \cdot \mathcal{A} \cdot \left(\frac{r_{\text{lock}}}{R_{\text{ship}}}\right)^{1/6} \cdot \left(\frac{\nu_{\text{field}}}{\nu_{\text{lock}}}\right)^2$$

where $N_c = n_\gamma \cdot V_c$ is the macroscopic coherent condensation degree of the system (the product of photon number density and coherence volume), and $R_{\text{ship}}$ is the effective radius of the spacecraft. A very large input power is used to make $N_c \gg (R_{\text{ship}}/r_{\text{lock}})^{1/6}$, forcing the overall value of $\mathcal{C}$ up into the activation region above 1.

**15.2 Phase-lock cavity energy-density equation:**

The energy density $\rho_E$ that must be maintained in the closed standing-wave cavity outside the spacecraft is:

$$\rho_E = \frac{1}{2}\left(\varepsilon_0 E^2 + \frac{B^2}{\mu_0}\right) = n_\gamma \cdot h\nu_{\text{lock}}$$

(Note: in an earlier version, the left-hand side $\frac{1}{8\pi}(E^2+B^2)$ was written in Gaussian units, while the right-hand side $n_\gamma h\nu_{\text{lock}}$ and the rest of the text (h, eV, nm, as) use SI, so the two sides of the same equation mixed two unit systems. It is now unified to SI.)

To maintain this high energy density in a steady state, the required critical continuous standing-wave input power $P_{\text{req}}$ is:

$$P_{\text{req}} = \frac{\rho_E \cdot S \cdot d}{\tau_{\text{decay}}}$$

**15.3 Attosecond topological rhythm condition:**

The pulse time spacing $\Delta t$ must strictly satisfy physical resonance at integer multiples of $17.8\text{ eV}$, to prevent decoherence-induced mass surges from tearing the spacecraft apart:

$$\Delta t = k \cdot 232 \text{ as} \quad (k \in \mathbb{N})$$

## 16. Six-Layer Worldview

Layer 1: Everything is space. Space is not a stage; it is the only entity.
Layer 2: Matter is a wound in space. Energy is the tension that repairs the wound.
Layer 3: The hexagonal totem. The 1/6-dimensional gap is the underlying code of all sixfold symmetry in nature.
Layer 4: Time is the unfolding of a helix. Space is not fully woven and can only spiral outward; this tendency to grow outward at the speed of light is time.
Layer 5: Black holes are entrances back to the origin. Impedance tends to infinity at extremely small scales / extremely high energies; a black hole is not a solid sphere but a spacetime paper clip leading to the unbroken ground state.
Layer 6: All things return to one. In this framework, gravity, electromagnetism, mass, and time are no longer distinct physical realities; all are projections, in different dimensions, of one thing: the right-handed helical divergence of space.

## 17. Three Routes Converging: The Gap Self-Concealment Theorem and Test Channels

Measuring D = 17/6 relies on measuring the nonlinear biases it imposes on other physical quantities as it emerges at different levels. This section gives the complete derivation of the gap self-concealment theorem and honestly flags the net reduction in falsifiability it entails.

**Gap self-concealment theorem.** The two effects share the same control parameter $\mathcal{C}(r,\nu) = \mathcal{A}\cdot(r_{\text{lock}}/r)^{1/6}\cdot(\nu/\nu_{\text{lock}})^2$, and $\mathcal{C}$ simultaneously modulates the activation depth of both:

- **Low excitation ($\mathcal{C}\ll1$, macroscopic low frequency)**: $D_{\text{eff}}\to3$, the Gaussian surface area returns to $r^2$, and flux dilution switches off; $\mathcal{Z}_{\text{eff}}\to\mathcal{Z}_0$, and impedance enhancement switches off. Both terms vanish simultaneously, so Newton holds trivially, without relying on cancellation.
- **High excitation ($\mathcal{C}\gg1$, $\nu\to\nu_{\text{lock}}$, nanometer scale)**: $D_{\text{eff}}\to17/6$, the Gaussian surface grows as $r^{11/6}$, and flux dilution biases the slope toward **−11/6** (shift +1/6); $\mathcal{Z}_{\text{eff}}\to\mathcal{Z}_0\cdot\mathcal{C}\propto r^{-1/6}$, and impedance enhancement biases the slope toward **−13/6** (shift −1/6). The two terms have the same form ($g = h = \mathcal{C}/(1+\mathcal{C})$), cancel exactly, and the slope returns to −2.

Effective-dimension interpolation: $D_{\text{eff}}(\mathcal{C}) = 3 - (1/6)\cdot\mathcal{C}/(1+\mathcal{C})$, which shares the same control parameter with $\mathcal{Z}_{\text{eff}} = \mathcal{Z}_0(1+\mathcal{C})$; both originate from the $D = 17/6$ helical fractal network. **Space uses changes in its own stiffness to hide its own dimensional deficit in statics** — the deficit shows itself only in dynamics (delay, dispersion, scattering geometry).

Exact slope: $d \ln F/d \ln r = -2 - \mathcal{C}\cdot\ln(r/r_{\text{lock}})/[36\cdot(1+\mathcal{C})^2]$. In the transition region ($\mathcal{C}\sim 1$, $r\sim r_{\text{lock}}$) the residual peaks at about ±0.032, about 1/5 of the magnitude of $\alpha$, which current gravitational measurement techniques cannot resolve at all.

**Statement of net reduction in falsifiability (must not be omitted)**

Relative to a single-mechanism form without the self-concealment mechanism, this framework has one explicit downgrade in falsifiability:

| Criterion | Single-mechanism form (no self-concealment) | Self-concealment mechanism (this framework) |
|---|---|---|
| Route 2 nanoscale gravity static slope | −13/6 ≈ −2.167 (deviates from Newton by 0.167) | −2 (Newton; neither effect activated) |
| Route 2 constraining power | Effective: if −2 is measured, Z-Model is falsified | Ineffective: −2 cannot distinguish Z-Model from Newton |
| Transition-region residual | No prediction | ≈ 0.032 (second-order small quantity, currently unmeasurable) |

This is not a calculation error but the logical cost of the self-concealment mechanism along Route 2: in return for "both effects sharing $\mathcal{C}$ gating and cancelling self-consistently across all frequency bands," the live refutation line of Route 2 disappears. **Route 1 (attosecond photoionization) is the only effective test channel.**

Accordingly, the three routes are reordered:

**Route 1 · Attosecond photoionization (measuring time) — primary criterion.** Scan 12–22 eV; after subtracting the standard Wigner / Coulomb–laser coupling delays, the residual delay rises with $(\nu/\nu_{\text{lock}})^2$. Microscopic mechanism (see §21): in the high-$\mathcal{C}$ window the electron effective mass drops transiently, $M_{\text{eff}} = M_0/(1+\mathcal{C})$, wave-packet dispersion changes accordingly, and the residual is $\Delta T \sim \mathcal{C}\cdot T_{\text{atomic}}$. Roughly estimated with the atomic unit of time $T_{\text{atomic}} \approx 24\text{ as}$ and the atomic-scale $\mathcal{C} \approx 3.31\mathcal{A}(\nu/\nu_{\text{lock}})^2$, at $\nu \to \nu_{\text{lock}}$ one has $\Delta T \sim 80\mathcal{A}\text{ as}$: if $\mathcal{A} \sim \mathcal{O}(1)$ the signal is large, and existing 1 as-level precision is sufficient to calibrate $\mathcal{A}$ directly or push it below 0.01. **This is the only near-term experiment on which the model can be cleanly staked.**

**Prediction layers of Route 1.** The two elements of this channel have different evidential status and must be stated separately:

| Element | Nature | Explanation |
|---|---|---|
| Residual rises with $(\nu/\nu_{\text{lock}})^2$; the fitted power exponent must hold at 2 | **Genuine prediction** | The power-law shape is derived from $\beta=2$ and the mass-flow mechanism and contains no adjustable degree of freedom; failure to observe it falsifies the frequency term |
| Window position falls at 17.83 eV | **Calibration result** | Converted from $T_{\text{lock}}=232$ as (§10.1); not a position computed by the model |
| Amplitude $\Delta T \sim 80\mathcal{A}$ as | **Contains a free parameter** | Proportional to the undetermined $\mathcal{A}$; does not by itself constitute an independent prediction |

The earlier statement "the only probe that falls naturally at $\nu_{\text{lock}}$" was open to the charge of circular reasoning — $\nu_{\text{lock}}$ is itself defined by the results of this class of calculation. It has been changed. **The falsifiable content of Route 1 is the shape and exponent of the power law, not the position of the window.**

**Route 2 · Nanoscale gravity (measuring gravity) — refutation line lost, downgraded to residual exploration.** The predicted deep-nanoscale static slope is exactly −2 (Newton), not because the two effects cancel but because neither effect is activated ($\mathcal{C}\ll1$, $\nu\to0$, both terms vanish simultaneously). Route 2 does not constitute an effective test — whether −2 or −2 ± a small deviation is measured, it cannot distinguish Z-Model from classical Newtonian gravity. Honest flag: Route 2 is a dud; this is the logical cost of the self-concealment mechanism. What remains observable is only the $\mathcal{O}(\alpha^2)$ residual slope shift in the transition window ($r\sim r_{\text{lock}}$, $\mathcal{C}\sim 1$), peaking at about ±0.032, far beyond existing technology. Given that gravitational measurement at 100 nm is itself still far beyond existing technology (the Casimir force exceeds gravity by more than ten orders of magnitude), Route 2 remains third priority.

**Route 3 · Phase-lock window scattering (measuring matter) — EUV probe.** The ultracold-atom scheme is killed by the frequency gate (kHz–MHz probes give $(\nu/\nu_{\text{lock}})^2 \sim 10^{-20}$), so it is redesigned to place the probe energy directly in the phase-lock window — **using a seeded extreme-ultraviolet free-electron laser (e.g., FERMI, whose operating range of 12–62 eV happens to cover 17.8 eV) for small-angle scattering, measuring the power law of the dynamic structure factor**. The prediction is a "switchable" fingerprint: when the probe energy sweeps through the 17.8 eV window, $S(q) \propto q^{-17/6}$; away from the window it returns to the conventional $q^{-3}$. Scattering measures the geometric dimension itself and does not go through the mechanical channel, so it **is not cancelled by gap self-concealment** — together with Route 1 it forms a dual dynamical criterion.

## 18. Z-Model Final Form

Z-Model: a cross-scale spacetime-impedance framework based on $\Delta N = -1$ topological breaking. Its static prediction is "Newton everywhere" (gap self-concealment: the two effects share $\mathcal{C}$ gating and vanish together or cancel together); all of its new physics lies in dynamical windows — delay, dispersion, relativistic momentum corrections, room-temperature coherence — concentrated near the phase-lock energy $E_{\text{lock}}=h/T_{\text{lock}}$. The derived equation sets of §13–15 and §21–24 constitute its system of consequences meshing with quantum mechanics and relativity.

### 18.1 Positioning Statement

The correct positioning of this framework is: **a cross-scale phenomenological scaling model with two input parameters**, not a first-principles theory. The two inputs and their status:

| Input | Value | Status |
|---|---|---|
| $\mathcal{A}$ | $\mathcal{O}(1)$, undetermined | Dimensionless coupling, calibrated by Route 1 |
| $T_{\text{lock}}$ | 232 as | **External input (a numerically computed value)**; cannot be derived from the framework (§10.2) |

Neither of the framework's two signature numbers is a derived result:

- $\alpha=1/6$ and $D=17/6$ are **axiomatic inputs**. An attempt to derive them from a sixfold chiral hyperbolic discrete group has been falsified ($\delta(\Gamma_6^\chi)\le1<17/6$; see the genealogy note in §9).
- $T_{\text{lock}}$ is an **external input (a numerically computed value)**, and because of the §20 decoupling clause it is structurally non-derivable (§10.2).

Consequently, $\beta=2$ (from helical rotational kinetic energy) and the operational definition of $\nu$ (from the §1.1 impossibility theorem) are **the only two genuinely derived results** within the framework; all other numerical values are conversions or consequences of the above inputs.

**This does not weaken the framework's testability, but it determines the boundary of its claims:** this paper does not claim to have unified quantum theory and gravity, nor to have derived any fundamental constant; it claims only to give a cross-scale scaling structure that is dimensionally self-consistent, macroscopically safe, and accompanied by six explicitly stated refutation lines. Among the test channels, Route 1 (the $\nu^2$ power-law shape of the attosecond residual) and Route 6 (the atom-independence of $T_{\text{lock}}$) take priority.

## 19. Verifiable Predictions and Refutation Conditions

First, macroscopic orbits: if any systematic deviation exceeding order $v^2/c^2$ is measured at astronautical scales, the model as a whole is falsified.

Second, the attosecond residual (main battleground): if the residual does not rise with $(\nu/\nu_{\text{lock}})^2$, or the fitted power does not point to 2, the frequency term is falsified; **if the residual is zero to 1 as precision, then $\mathcal{A} < 0.01$, the model is retained, but all engineering and application consequences of §21–24 become void**.

Third, nanoscale gravity: Route 2 predicts a slope of exactly −2 (Newton; neither effect activated), which does not constitute an effective test — whether −2 or −2 ± a small deviation is measured, it cannot distinguish Z-Model from classical Newtonian gravity. In the single-mechanism form, Route 2 once had refuting power (measuring −2 would falsify); after introducing the self-concealment mechanism this refutation line is lost, as made explicit in §17. The transition-region residual ($\mathcal{C}\sim 1$, $r\sim r_{\text{lock}}$) peaks at $\approx 0.032$ and is currently unmeasurable. If deep-nanoscale measurements persistently yield −13/6 or −11/6 (whichever side the bias is on), this indicates that only one of the two mechanisms is present, the self-concealment mechanism does not exist, and the model reverts to the single-mechanism form to be rewritten.

Fourth, scattering dimension: if the S(q) power law within the EUV phase-lock window does not read out 17/6, or if 17/6 is also read out outside the window (not switchable), the fractal degree of freedom is falsified.

Fifth, the Rydberg constant (Route 5, see addendum): if Clause Zero is adopted ($\nu$ ≡ external driving-field frequency), then $\mathcal{C}\equiv0$ in a dark environment and this item is identically zero; if $\nu$ is reinterpreted as any intrinsic frequency, the $4.2\times10^{-15}$ precision of hydrogen 1S–2S immediately pushes $\mathcal{A}$ below $10^{-13}$. The role of this item is to lock down the definition of $\nu$.

**Sixth, the atom-independence of $T_{\text{lock}}$ (Route 6, the lowest-cost item).**

The framework treats $T_{\text{lock}}$ as a fundamental scale **of spacetime** (§3, §10.1). If this positioning is correct, it **must be independent of the atom used for detection**. But 232 as comes from the solution of the time-dependent Schrödinger equation for helium (§10.1). This yields a verdict that requires no new apparatus:

> Repeat the same class of experiment as Phys. Rev. Lett. **133**, 163201 on other atoms such as **neon and argon**, and measure the "entanglement birth-time difference."
>
> - **If this time changes with the atom** ⇒ it is an atomic-physics quantity, not a spacetime constant. $\mathcal{C}(r,\nu)$ would become a quantity dependent on the probe atom, in direct contradiction with its positioning as an "effective spacetime impedance" ⇒ **the scale anchoring of this framework is falsified as a whole**.
> - **If the same value is obtained on different atoms** ⇒ the framework gains its first piece of supporting evidence genuinely independent of the original fit.

**Honest prior assessment:** this delay originates in the Hamiltonian of a specific atom and is very likely to change when the atom is changed, so this item will most probably give a **negative result**. It is nonetheless stated explicitly — a test expected to be lost carries more weight than any evasion.

This item requires no new apparatus, only a change of target gas and a rerun; of all six refutation lines it is the one with the lowest execution cost and the strongest discriminating power, and it is recommended that it be scheduled first.

## 20. 𝒵–Electromagnetic Decoupling Clause and Charge Topology Clause

**Decoupling clause.** If there were any "structural bridge between G and the fine-structure constant $\alpha_{\text{em}}$" (such as something of the form $G = a^2\mu_0$), the flow of $\mathcal{Z}$ would force $\alpha_{\text{em}}$ to flow: $a_{\text{eff}} = a_0\sqrt{1+\mathcal{C}}$. But at atomic scale and at $\nu_{\text{lock}}$, $\mathcal{C} \approx 3.31\mathcal{A}$, and $\mathcal{A} \sim \mathcal{O}(1)$ would make $\alpha_{\text{em}}$ drift by $\sim165\%$ — long since excluded by XUV precision spectroscopy. **Existing data already decide this; no new experiment is needed**: either $\mathcal{A} \ll 10^{-6}$ (which kills the Route 1 signal along with it), or decoupling. This framework formally adopts decoupling: **the flow of 𝒵 occurs only in the gravity–impedance sector, and the electromagnetic sector is exempt; all G–$\alpha_{\text{em}}$ numerical bridges (including the 0.26% coincidence $a^2\mu_0 \approx G$) are regarded only as macroscopic numerology and are given no structural status**. Both cost and benefit are stated: the model henceforth remains silent on all electromagnetic precision measurements (its predictions are uniformly zero drift), in exchange for the right of $\mathcal{A} \sim \mathcal{O}(1)$ to survive.

**Charge topology clause.** Charge is the winding number of a helical defect: $q = e\cdot N_w$, $N_w \in \mathbb{Z}$. The winding number is topologically protected and does not flow with $\mathcal{C}$ — this also answers an old question: **why charge is quantized while mass is not**. Charge is an integer topological charge; mass is the continuous phase-lock energy of a defect (which flows with the ambient impedance; see §21). Refutable: any experimental sign of "charge drifting with scale/frequency" (the current upper limit on electron–proton charge equality is $10^{-21}$) kills this clause.

## 21. Propulsion Extension: Conditional Derivation of Effective-Mass Flow

**Premise axiom: the mass-geometry axiom — mass is the quotient of a spatial geometric quantity and spacetime impedance.** This is an axiom borrowed from Zhang Xiangqian's system and modified; its static form is the local equation of §7.

**Derivation (three steps):**
1. μ-degeneracy (§7): the observable in the gravitational sector is the product m𝒵, $m\cdot\mathcal{Z}_{\text{eff}} = rv^2(1-v^2/c^2)$;
2. The geometric side $rv^2(1-v^2/c^2)$ is locked by orbital geometry and does not flow with impedance;
3. When $\mathcal{Z}_{\text{eff}} = \mathcal{Z}_0(1+\mathcal{C})$ flows, mass must compensate inversely:

$$M_{\text{eff}} = M_0\cdot\mathcal{Z}_0/\mathcal{Z}_{\text{eff}} = M_0/(1+\mathcal{C})$$

As $\mathcal{C} \to 0$, $M_{\text{eff}} = M_0$ (common sense); when frequency is artificially raised and phase-locked so that $\mathcal{C} \gg 1$, $M_{\text{eff}}$ tends nonlinearly to zero. **It is not a guess; it follows necessarily from the mass-geometry axiom plus impedance flow** — to kill it, kill that axiom; the target is clear.

**Meshing with Route 1:** at the instant of photoionization, the electron, at atomic scale and in the high-$\mathcal{C}$ window near the $\nu_{\text{lock}}$ frequency, briefly experiences $M_{\text{eff}} < M_0$; wave-packet group velocity and dispersion change, accumulating a delay residual proportional to $\mathcal{C} \propto \nu^2$ — **the signal shape of Route 1 is inferred back from the mechanism of this section and has the same form as the phenomenological expression of §5. Once attosecond experiments calibrate $\mathcal{A}$, all consequences of this section become quantitative; if $\mathcal{A}$ is pushed down, this section is out as a whole.**

**Equivalence-principle constraint:** the $10^{-15}$-level null result of the MICROSCOPE satellite lies in the low-frequency region and is naturally satisfied by the frequency gate, so it poses no threat; the equivalence-principle violation predicted in this section carries a frequency fingerprint — the degree of violation is $\propto$ the spectral weight of the material's internal mode spectrum near 17.8 eV, which gives future atom interferometers a correlation to look for.

**Topological long-range correlation in phase-locked lattices** is a long-term extrapolation and is not part of the refutation core.

## 22. Light-Speed Propulsion Engineering and Core Hardware

To achieve the macroscopic mass dissolution and geodesic flow described in §14–15, overturning conventional reaction-mass spaceflight, a non-contact-friction "plasma topological generator" must be built. The core system for light-speed flight consists of four physical devices:

1. **Seeded EUV FEL Arrays**
   - **Engineering role:** the spacecraft's "topological heart."
   - **Technical parameters:** high-energy ray arrays miniaturized using laser wakefield acceleration (LWFA), outputting along the spacecraft's central axis a fully coherent photon stream precisely locked at **17.8 eV**, serving as the energy source for the entire external phase-lock field of the spacecraft.
2. **Non-neutral Topological Plasma Shield**
   - **Engineering role:** a perfect photonic crystal and standing-wave cavity wall.
   - **Technical parameters:** extreme-ultraviolet light is very easily absorbed by solid matter, so the exterior of the spacecraft must be enveloped in a pure electron cloud confined by a strong magnetic field. This shield forms a specific artificial lattice that totally reflects 100% of EUV photons, forming a high-density $\mathcal{C}_{\text{macro}}$ impedance manifold around the spacecraft.
3. **Attosecond Optical Clock Synchronizer**
   - **Engineering role:** the hub for navigation safety and relativistic balancing.
   - **Technical parameters:** senses the spacecraft's Lorentz factor $\gamma$ in real time and, using **232 as** as the timing reference, feeds frequency and phase back to the extreme-ultraviolet emitter array, ensuring that $1+\mathcal{C}=k\gamma$ is dynamically satisfied. If desynchronization exceeds the attosecond level, the instantaneous restoration of mass will cause the spacecraft to disintegrate.
4. **Impedance Gradient Deflector**
   - **Engineering role:** reaction-mass-free attitude control and helm.
   - **Technical parameters:** by asymmetrically controlling the plasma density and thickness on different sides of the shield, it artificially creates the spacetime impedance gradient $\partial\ln(1+\mathcal{C})$ required by the equation $\Gamma^\mu_{\alpha\beta}(\mathcal{C})$. The spacecraft will turn smoothly along artificial geodesics, as if gliding down a warped waterfall of space (for an order-of-magnitude estimate of the required gradient see §24.4).

## 23. Derived Formulas for Topological Coherence and Room-Temperature Superconductivity

Superconductivity is essentially a macroscopic quantum coherent state. Introducing the electron effective-mass flow $M_{\text{eff}} = M_0/(1+\mathcal{C})$ into the classical mathematical framework of superconductivity reveals that room-temperature superconductivity is not merely a matter of materials-chemistry composition but a problem of geometric and topological field modulation. **Room-temperature superconductivity is in essence a by-product of "gravitational shielding / mass dissolution" at microscopic scales.**

### 23.1 Fractal-Gated Ginzburg–Landau Equation

Substituting the impedance flow into the Cooper-pair kinetic-energy term of the classical Ginzburg–Landau equation, and replacing the conventional gradient operator with a fractal operator, gives a new superconducting-state equation:

$$a_{\text{GL}}(\mathcal{C}, T)\,\psi + b_{\text{GL}}\,|\psi|^2 \psi + \frac{1+\mathcal{C}}{2M_0} \left(-i\hbar \nabla_{D_{\text{eff}}} - qA\right)^2 \psi = 0$$

(Note: the standard coefficient symbols $\alpha,\beta$ of the Ginzburg–Landau equation clash with this framework's two signature exponents $\alpha=1/6$ and $\beta=2$ of §8/§10, which would very easily be misread in peer review; this section therefore writes them as $a_{\text{GL}}$ and $b_{\text{GL}}$. $\nabla_{D_{\text{eff}}}$ is the gradient operator corresponding to the running fractal Laplacian of §13.3.)

**Physical effect:** The factor $(1+\mathcal{C})$ appearing in the kinetic-term coefficient indicates that when a material is placed in an extremely high-frequency standing-wave field, the coherent stability of the wave function $\psi$ can be forcibly maintained even at room temperature.

### 23.2 Critical-Temperature Flow Formula

The superconducting critical temperature is no longer a fixed intrinsic constant, but transitions dynamically with the activation depth:

$$T_c(\mathcal{C}) = T_{c0} \cdot \sqrt{1 + \mathcal{C}}$$

**Physical effect:** By raising the local value of $\mathcal{C}$ with external equipment (e.g., $1+\mathcal{C} = 100$), a material that originally has a superconducting phase only at very low temperature (e.g., 30K) can have its effective critical temperature amplified tenfold, jumping directly into the room-temperature range (300K).

### 23.3 Topological Condition Against Thermal Fluctuations

For phonon scattering at room temperature to be unable to destroy the electron pairing gap, the energy floor under impedance modulation must satisfy:

$$\Delta_0 \cdot (1 + \mathcal{C}) > k_B \cdot T_{\text{room}}$$

**Physical effect:** As long as the local standing-wave energy density provided by the external high-frequency field is high enough, the microscopic superconducting gap can be topologically "locked," becoming completely immune to destruction by room-temperature thermal fluctuations. Room-temperature superconductivity is thereby converted into a pure engineering problem of high-frequency field-strength control.

## 24. Derived Equation Set: Formal Derivations Addressing Real-World Problems

**Methodological statement:** All equations in this section use only existing axioms and operators — mass flow $M_{\text{eff}} = M_0/(1+\mathcal{C})$ (§21), impedance flow $\mathcal{Z}_{\text{eff}} = \mathcal{Z}_0(1+\mathcal{C})$ (§5), running dimension $D_{\text{eff}}(\mathcal{C})$ (§8), and the decoupling clause and charge topology clause (§20) — and introduce no new parameters. This section therefore adds no degrees of freedom to the model, only exposure: every application equation is a new potential refutation line. **All quantitative force hangs on a single number: Route 1's calibration of $\mathcal{A}$. If $\mathcal{A}$ is pushed below 0.01, this section is out as a whole together with §21.**

### 24.1 Fractal-Gated Tunneling Rate Equation (Quantification of the Qualitative Prediction of §13.1)

The Gamow exponent for WKB barrier penetration is proportional to $\sqrt{M}$. Substituting $M_{\text{eff}}$:

$$G(\mathcal{C}) = \frac{2}{\hbar}\int \sqrt{2M_{\text{eff}}\,(V-E)}\;dx = \frac{G_0}{\sqrt{1+\mathcal{C}}}\,, \qquad P(\mathcal{C}) = e^{-G_0/\sqrt{1+\mathcal{C}}}$$

Penetration enhancement ratio:

$$\frac{P(\mathcal{C})}{P(0)} = \exp\!\left[ G_0\left(1 - \frac{1}{\sqrt{1+\mathcal{C}}}\right) \right]$$

**Physical effect:** $G_0$ sits in the exponent — for typical chemical surface reactions $G_0 \sim 10$–$30$, and for light-nucleus Coulomb barriers $G_0$ is of order $10^2$. Even with $\mathcal{C} \sim 1$ (enhancement factor $1-1/\sqrt{2} \approx 0.29$), the rate enhancement reaches the $e^{3}$–$e^{30}$ level. Application directions, ordered by $G_0$ from small to large: ① field-controlled catalysis — lighting up the tunneling channel of surface reactions inside a 17.8 eV standing-wave cavity, so that reaction rate becomes a knob of field strength; ② tunneling electronic devices — field-controlled switching of flash-memory writing and tunnel junctions; ③ tunneling gain in the ignition window of light-nucleus fusion — this is isomorphic with the room-temperature superconductivity of §23: both rewrite a "materials/temperature problem" as a "field-control problem." **Refutation line:** if any EUV pump–probe surface-reaction-rate experiment fails to detect exponential enhancement in the region where $\mathcal{C}$ is significant, this item and the mass flow of §21 are out together.

### 24.2 Variable-Mass de Broglie Relation and Interference Diagnostics

The momentum $p = M_{\text{eff}} v$ directly rewrites the de Broglie wavelength and group velocity:

$$\lambda_{\text{eff}} = \frac{h}{M_{\text{eff}}\,v} = \lambda_0\,(1+\mathcal{C})\,, \qquad v_g = \frac{\hbar k\,(1+\mathcal{C})}{M_0}$$

**Physical effect:** This is an equivalent reading of the Route 1 delay residual (the wave packet "becomes lighter and faster"), but it also opens a test line independent of photoionization: **electron interference-fringe diagnostics**. In electron double-slit / holographic interference under EUV pumping, the fringe spacing should broaden by a factor of $(1+\mathcal{C})$ — the interference geometry reads out $M_{\text{eff}}$ directly, without depending on the subtraction model of the delay fit. Alongside Route 1 and Route 3, it constitutes a fourth test channel (Route 4), and it shares the calibration constant $\mathcal{A}$ with Route 1: if the two routes' readings disagree, the model is internally contradictory and directly falsified.

### 24.3 Flow Transport Equations: Mobility, Electrical Conductivity, Thermal Conductivity

The carrier relaxation time $\tau$ is determined by scattering geometry and does not flow with impedance (the same logic as "the geometric side is locked" in §21); the mobility and conductivity are then:

$$\mu(\mathcal{C}) = \frac{e\tau}{M_{\text{eff}}} = \mu_0\,(1+\mathcal{C})\,, \qquad \sigma(\mathcal{C}) = \sigma_0\,(1+\mathcal{C})$$

Via the Wiedemann–Franz law, the electronic thermal conductivity is amplified in step:

$$\kappa_e(\mathcal{C}) = L\,\sigma(\mathcal{C})\,T = \kappa_0\,(1+\mathcal{C})$$

**Self-consistency with the decoupling clause:** what flows is carrier inertia (mass in the gravity–impedance sector); the charge $e$ and the fine-structure constant do not change at all — the electromagnetic exemption of §20 is not touched. **Physical effect:** ① EUV-gated ultrafast electronics — mobility becomes a knob of field strength, and the $(1+\mathcal{C})$ amplification of normal-state conductivity and the superconducting state of §23 form the two ends of the same mechanism (when $\mathcal{C}$ is insufficient to lock the gap one obtains an "enhanced conductor"; when sufficient, a superconductor); ② field-controlled heat dissipation — the thermal conductivity at chip hot spots increases by $(1+\mathcal{C})$, turning thermal management from materials science into field-control engineering.

### 24.4 Weak-Field Quantitative Form of Artificial Acceleration (Engineering Reading of the §14.2 Geodesic Equation)

Taking the weak-field, low-velocity limit of the connection flow equation of §14.2 ($g_{\mu\nu} \approx \eta_{\mu\nu}$, static $\mathcal{C}$ field), the geodesic equation gives the autonomous acceleration:

$$\vec{a} \approx -\frac{c^2}{2}\,\nabla \ln(1+\mathcal{C})$$

**Engineering reading:** to obtain an acceleration of 1g, the required gradient is only

$$|\nabla \ln(1+\mathcal{C})| = \frac{2g}{c^2} \approx 2.2\times10^{-16}\ \text{m}^{-1}$$

Across a spacecraft span of $R_{\text{ship}} = 10$ m, $\ln(1+\mathcal{C})$ on the two sides of the shield need only differ by an asymmetry of $\sim 2\times10^{-15}$. The enormous lever of $c^2$ means: **the engineering difficulty of the deflector (the fourth device of §22) lies not in the "strength" of the gradient but in its "purity"** — fluctuation noise in plasma-density control must be suppressed below $10^{-15}$ relative precision, otherwise the spacecraft's attitude will be kicked about randomly by noise gradients. This expression turns the qualitative hardware description of §22 into a control specification with numerical targets, and incidentally explains why autonomous acceleration has never been observed in everyday environments (where natural $\mathcal{C}$ gradients are extremely gentle and $\mathcal{C}\approx0$): although the gradient lever is large, the natural background of $\ln(1+\mathcal{C})\approx\mathcal{C}\approx10^{-50}$ order suppresses it completely.

### 24.5 Gravitational-Wave Impedance Dispersion Equation (Self-Consistency Check + Long-Term Fingerprint)

A direct consequence of the high-frequency-corrected field equations (§13.2) for gravitational-wave propagation: the wave speed is dragged by the local impedance flow,

$$\frac{c_{\text{gw}}(\nu)}{c} = \frac{1}{\sqrt{1+\mathcal{C}(r,\nu)}} \approx 1 - \frac{\mathcal{C}}{2}$$

**Self-consistency check (the model passes existing data):** in the LIGO/Virgo band $\nu \sim 10^2$–$10^3$ Hz and at astronomical scales $r$, $\mathcal{C}$ is pushed by the frequency-squared term below order $10^{-26}$ — the constraint $|c_{\text{gw}}-c|/c < 10^{-15}$ from GW170817 is automatically satisfied, and the model is untouched by existing gravitational-wave data. **Long-term fingerprint:** if MHz–GHz high-frequency gravitational-wave detectors appear in the future, dispersion $\propto \nu^2$ is Z-Model's only fingerprint in the gravitational-wave channel; if dispersion not following $\nu^2$ is measured, or zero dispersion is measured in the region where the effect should be manifest, this item is falsified.

### 24.6 Josephson Identity Clause (Authenticity Discriminator for §23)

The Josephson frequency $f_J = 2eV/h$ contains only the charge $e$ and the Planck constant $h$: $e$ is protected by the charge topology clause (§20), and $h$ is not within any flow operator. Therefore, for any $\mathcal{C}$:

$$f_J(\mathcal{C}) \equiv \frac{2eV}{h} = f_J(0)$$

**Physical effect:** If field-controlled room-temperature superconductivity (§23) is actually realized, its Josephson frequency must be **strictly identical** to that of conventional low-temperature superconductors — without the slightest difference. This equips any future "room-temperature superconductivity claim" with an authenticity discriminator built into Z-Model: if the Josephson frequency drifts, it is not this mechanism (or the model is internally contradictory and falsified as a whole); only an identical frequency together with $T_c$ running with field strength as $\sqrt{1+\mathcal{C}}$ constitutes the complete fingerprint of fractal-gated superconductivity.

### 24.7 Summary Table of Application Thresholds

| Application | Load-bearing equation | Required conditions | Prerequisites |
|---|---|---|---|
| Field-controlled catalysis / tunneling devices | §24.1 | $\mathcal{C} \gtrsim 0.1$, local EUV standing wave | Route 1 calibration $\mathcal{A}\sim\mathcal{O}(1)$ |
| Electron interference diagnostics (Route 4) | §24.2 | Existing electron holography + EUV pumping | None (is itself a test) |
| EUV-gated electronics / field-controlled heat dissipation | §24.3 | $\mathcal{C} \gtrsim 1$ sustained standing wave | Route 1 calibration + §24.1 verification |
| Room-temperature superconductivity | §23 | $1+\mathcal{C} \sim 10^2$ | Same as above + Josephson identity (§24.6) |
| Reaction-mass-free propulsion / artificial gravity | §24.4 | $\mathcal{C}_{\text{macro}}$ gradient purity $10^{-15}$ | All preceding items + §15 macroscopic coherence |
| Light-speed flight | §14.4 | $1+\mathcal{C} = k\gamma$ attosecond phase-lock | All preceding items |
| High-frequency gravitational-wave dispersion | §24.5 | MHz–GHz detectors (not yet existing) | Long-term |

The threshold table is also a dependency chain: all downstream applications hang on Route 1's calibration of $\mathcal{A}$, and if the refutation line of any link in the chain is triggered, everything downstream of it is out. This is the fulfillment of this section's commitment to "add no degrees of freedom, only exposure."

# 11 · The Vacuum: Huge Numbers, Tiny Effects, and Physics' Biggest Embarrassment

> Empty space isn't empty. But the most naive estimate of its energy is wrong by a factor of 10¹²³, and nobody knows why. That's the real unsolved mystery.

**Status:** ✅ Established (zero-point energy, Casimir effect, vacuum fluctuations). 🔴 Unsolved (the cosmological constant problem). 📜 Unexplained coincidence (the 10⁴² "large numbers"). ❌ Not supported: extracting usable energy from the vacuum ground state.

---

## What everyone wishes they'd noticed sooner

Quantum physics says the vacuum hums with fluctuations. Some effects are measured: the Casimir force ([04](04-shape-picks-the-notes.md)), the Lamb shift in hydrogen, and the anomalous magnetic moment of the electron (predicted and measured to about 12 digits).

If you add up zero-point energy all the way down to the Planck scale, you get a density of about **10⁹³ g/cm³**. But the energy density that actually drives the universe's accelerating expansion (dark energy) is about **10⁻³⁰ g/cm³**. The mismatch is a factor of roughly **10¹²³**. It's been called "the worst theoretical prediction in the history of physics."

This is the true version of the "idiot realization": **every physicist knows something basic about empty space is badly misunderstood**, and nobody has fixed it yet.

## Explain it to a kid

The ocean's surface looks flat from an airplane, but up close it's churning with waves. Empty space is like that. Up close, at sizes far smaller than an atom, it jiggles.

Here's the puzzle. When scientists use their best math to add up all that jiggling, they get a number so huge that the universe should have blown itself apart instantly. When they measure how hard space is actually pushing, it's a teeny tiny push. It's like predicting a hurricane and finding a breeze so faint you'd need a trillion-trillion-trillion-trillion times more sensitive instruments to feel it. Figuring out why is one of the biggest open problems in science.

## Examples of vacuum effects that are real and measured

- **Casimir force:** plates pulled together by the vacuum ([04](04-shape-picks-the-notes.md)).
- **Lamb shift (1947):** hydrogen's energy levels are nudged by vacuum fluctuations. This measurement launched modern quantum electrodynamics.
- **Spontaneous emission:** an excited atom emits light *because* of vacuum fluctuations. Put the atom in a small enough cavity that removes the right modes and emission slows down (cavity QED; Haroche, Nobel Prize 2012).
- **Hawking radiation** (predicted, not yet observed from real black holes; analogs seen in lab fluids).

## The numbers (computed by `tools/big_numbers.py`)

| Quantity | Value |
|---|---|
| Planck length $\sqrt{\hbar G/c^3}$ | 1.616 × 10⁻³⁵ m |
| Planck time | 5.39 × 10⁻⁴⁴ s |
| Planck density $c^5/(\hbar G^2)$ | 5.2 × 10⁹³ g/cm³ |
| Nuclear density | ~2 × 10¹⁴ g/cm³ |
| Observed dark-energy density | ~6 × 10⁻³⁰ g/cm³ |
| Mismatch | ~10¹²³ |

## The 10⁴² coincidence

The electric force between two electrons is **4.2 × 10⁴²** times stronger than the gravitational force between them. The size of the observable universe (Hubble radius, about 1.4 × 10²⁶ m) divided by the classical electron radius (2.8 × 10⁻¹⁵ m) is about **5 × 10⁴⁰**.

Two unrelated-seeming ratios both land near 10⁴⁰–10⁴². Weyl (1919), Eddington, and especially **Paul Dirac (1937)** wondered if this was a clue. Dirac's "Large Numbers Hypothesis" suggested it's no accident, which would require the gravitational constant $G$ to *decrease* as the universe ages.

**It was tested, and it failed.** Lunar laser ranging (bouncing lasers off mirrors left by Apollo astronauts) shows $G$ changes by less than about 1 part in 10¹² per year. Dirac's version would need about 1 part in 10¹⁰. Most physicists now think the coincidence is partly anthropic (we exist at a time when stars have formed, which ties the age of the universe to atomic constants), as Robert Dicke argued in 1961. Why gravity is *so* weak compared to other forces, the **hierarchy problem**, is still open.

## The grown-up version

A free field's vacuum energy is a sum over modes, $E_0 = \sum_{\mathbf{k}} \tfrac12\hbar\omega_{\mathbf{k}}$. With a cutoff at wavenumber $k_{\max}$,

$$
\rho_{\text{vac}} \sim \frac{\hbar\, c\, k_{\max}^4}{16\pi^2}.
$$

With $k_{\max}\sim 1/\ell_P$ this gives roughly the Planck density. Observations (supernovae, the cosmic microwave background, and baryon acoustic oscillations) give $\Lambda$ corresponding to $\rho_\Lambda \approx 6\times10^{-27}$ kg/m³. Proposed resolutions include supersymmetry (which would partly cancel the sum, but hasn't been found at the LHC), anthropic selection in a multiverse (Weinberg predicted roughly the right size of $\Lambda$ this way in 1987), and modified gravity. Nothing is settled.

## Where the original notes went too far

- ✅ "The vacuum has enormous formal energy density near the Planck scale": **true as a naive estimate.** (The notes said 10⁹⁵ g/cm³. The standard figure is about 5 × 10⁹³.)
- ✅ "The 10⁴² ratio appeared to Feynman and others as a clue": **true.** Feynman discussed it in his *Lectures on Gravitation*.
- ❌ "That enormous density is an ocean of usable pressure": **not supported.** The vacuum is the **lowest** energy state by definition. Energy can only be extracted from *differences* between states. You can't lower something below its floor. (Casimir cavities give a one-time, tiny, conservative force.)
- ❌ "10⁴² proves electricity is compressed gravity": **not supported.** Nobody has turned it into a working theory that predicts anything new, and the version that did make a prediction (Dirac's) was falsified.
- ❌ "Quantum foam wormholes connect every point, making distance an illusion": quantum foam (Wheeler, 1955) is a **hypothesis** about the Planck scale with no direct evidence. Gamma-ray burst timing from the Fermi telescope has already ruled out some foam models that would blur light over cosmic distances.

## Try it

```bash
python tools/big_numbers.py
```

Every number on this page is printed by that script from fundamental constants. Change the inputs and see how sensitive each one is.

## Read more

- S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* 61, 1 (1989). The classic review.
- P. A. M. Dirac, "The Cosmological Constants," *Nature* 139, 323 (1937).
- R. H. Dicke, "Dirac's Cosmology and Mach's Principle," *Nature* 192, 440 (1961).
- J. G. Williams et al., "Progress in lunar laser ranging tests of relativistic gravity," *Phys. Rev. Lett.* 93, 261101 (2004).
- Fermi LAT & GBM Collaborations, *Nature* 462, 331 (2009). (Constraints on Lorentz-violating quantum-foam models.)

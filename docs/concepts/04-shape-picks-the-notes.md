# 04 · The Shape of the Container Picks the Notes

> You don't need to push every grain of sand into a pattern. Shape the container, and the vibration does the arranging for you.

**Status:** ✅ Established (eigenmodes, cavity physics, Casimir effect). ❌ Not supported: Casimir "propulsion" or free energy.

---

## What everyone wishes they'd noticed sooner

A drum, a guitar body, a microwave oven, a laser, and an atom all follow one rule: **the boundary decides which vibrations are allowed.** Those allowed vibrations are called *eigenmodes*. Change the shape, and you change the menu of possible notes, often without adding any energy at all.

This is geometry doing physical work every day. Engineers use it constantly: acoustic designers shape concert halls, antenna designers shape metal, photonics engineers shape glass at the nanoscale to trap light.

## Explain it to a kid

Sprinkle sand on a metal plate and play a violin bow along its edge. The sand jumps off the shaking parts and collects on the lines that stay still, making stars, grids, and flowers. A different note gives a different picture.

You didn't place a single grain. **The shape of the plate and the note together drew the picture.** Round plates make rings. Square plates make grids. Nature is full of "drawings" made this way.

## Examples you already know

- **Chladni figures** (1787). Sand on vibrating plates. Ernst Chladni toured Europe with them, and Napoleon funded a prize to explain them. Sophie Germain won it.
- **Musical instruments.** A flute and a violin playing the same note sound different because their shapes favor different overtones.
- **Your microwave oven** is a metal box sized so 2.45 GHz waves form standing patterns. That's why it has hot and cold spots, and why the plate turns.
- **Atoms.** Electron orbitals (s, p, d, f) are the "Chladni figures" of the electric field around a nucleus. They are spherical harmonics, the allowed vibration shapes on a sphere. The whole periodic table is organized by them.
- **"Can one hear the shape of a drum?"** Mark Kac asked this in 1966. The answer, found in 1992, is *almost*: two different drum shapes can have exactly the same notes, but it's rare. Shape and sound are deeply tied.

## The grown-up version

For a wave $\psi$ confined to a region $\Omega$, the allowed modes solve the Helmholtz equation

$$
\nabla^2\psi + k^2\psi = 0,\qquad \psi|_{\partial\Omega}=0 \ \text{(Dirichlet) or } \partial_n\psi|_{\partial\Omega}=0\ \text{(Neumann)} .
$$

Only a discrete set of $k_n$ values fits. The boundary shape completely determines that spectrum. Weyl's law says that asymptotically the number of modes below $k$ depends on the region's **volume**, with corrections from its **surface area**, so geometry is literally audible.

### The Casimir effect: boundaries change the vacuum

Quantum field theory says empty space has zero-point fluctuations in every mode. Put two uncharged metal plates a distance $a$ apart, and the long-wavelength modes between them are excluded. The result is an attractive pressure:

$$
P = -\frac{\pi^2 \hbar c}{240\,a^4}.
$$

Hendrik Casimir predicted it in 1948. Steve Lamoreaux measured it in 1997, and it's now measured to about 1% accuracy. It matters for micro-machines (MEMS), where it can make tiny parts stick together.

| Gap between plates | Casimir pressure |
|---|---|
| 1 µm | 0.0013 Pa (about a hundred-millionth of air pressure) |
| 100 nm | 13 Pa |
| 10 nm | 1.3 × 10⁵ Pa (about atmospheric pressure) |

*(Computed by `tools/big_numbers.py`.)*

## Where the original notes went too far

- ✅ "Boundaries modify vacuum fluctuations": **true** (Casimir effect).
- ✅ "Geometry, not brute force, can determine patterns": **true** (eigenmodes, and it's a good engineering insight).
- ❌ "An asymmetric cavity makes the vacuum push a craft with zero fuel": **not supported.** A closed system can't push on itself. Momentum conservation (concept [01](01-symmetry-is-conservation.md)) comes from the uniformity of space and applies to vacuum stresses too. Real proposals for vacuum thrust, most famously the "EmDrive," were traced to measurement artifacts (Tajmar et al., Dresden, 2021).
- ❌ "Vacuum energy can be harvested": the Casimir force is **conservative**. Letting plates snap together once releases a tiny, finite energy. Pulling them apart costs it back. No cycle yields net energy.
- 🟡 The **dynamical Casimir effect** is real: a boundary moving at near light speed turns virtual photons into real ones (Wilson et al., *Nature* 2011, using a superconducting circuit). But the photons' energy comes from whatever moves the boundary.

## Try it

```bash
python tools/chladni.py 3 5
python tools/chladni.py 2 7 --pgm   # writes an image you can open
```

Then build a real one: see [experiments/E001-chladni-plate.md](../../experiments/E001-chladni-plate.md).

## Read more

- M. Kac, "Can one hear the shape of a drum?", *Amer. Math. Monthly* 73 (1966).
- S. K. Lamoreaux, *Phys. Rev. Lett.* 78, 5 (1997).
- C. M. Wilson et al., "Observation of the dynamical Casimir effect in a superconducting circuit," *Nature* 479, 376 (2011).
- M. Tajmar et al., "High-Accuracy Thrust Measurements of the EMDrive," Space Propulsion Conference (2021).

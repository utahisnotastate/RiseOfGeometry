# 07 · Topology: Why Some Things Come in Whole Numbers

> Some properties of matter can't change a little bit. Like the number of holes in a donut, they can only jump. That makes them astonishingly precise.

**Status:** ✅ Established (topological phases of matter, Nobel Prize 2016; quantum Hall effect, Nobel Prizes 1985 and 1998). 📜 Historical: Kelvin's "atoms as knots." ❌ Not supported: transmuting elements by "re-tying" them.

---

## What everyone wishes they'd noticed sooner

Geometry cares about exact shapes. **Topology** only cares about what can't be changed without cutting or gluing. A coffee mug and a donut are "the same" to a topologist (one hole each), but a donut and a pretzel are not.

That sounds like a party trick. It turned out to be one of the biggest ideas in 20th-century physics: some properties of matter are **topological numbers**, so they come out as exact integers no matter how messy, dirty, or imperfect the material is. The quantized Hall resistance is so exact (better than one part in a billion) that since 2019 **it has been used to define the kilogram and the ohm.**

## Explain it to a kid

Take a rubber band and a rubber ring. You can stretch the band, squish it, or twist it, but it always has **one** hole. To get zero holes or two holes, you'd have to cut it. There's no way to have "one and a half" holes.

Some materials are like that inside. Electrons flowing through them carry a hidden count, like the number of holes, that can't be 1.5 or 1.01. It's exactly 1, or exactly 2. Because nothing gentle can change it, scientists use it as a perfect ruler.

## Examples you already know (or will soon)

- **Knots in a necklace.** You can't untie a true knot without opening the clasp. That's topology.
- **Hair whorls.** The *hairy ball theorem* says you can't comb a hairy ball flat everywhere; there's always at least one whorl. It's also why there's always somewhere on Earth where the wind isn't blowing.
- **Möbius strip.** One side, one edge. Cut it down the middle and you get one longer loop, not two.
- **The kilogram.** Since 2019 it's defined through Planck's constant, measured with Kibble balances that use the quantum Hall effect.
- **Smoke rings and water vortices.** In 2013, Kleckner and Irvine (University of Chicago) 3D-printed knotted wings to create **knotted vortices in water** and watched how they untie. The untying happens only at specific "reconnection" events, just as topology predicts.

## The grown-up version

In a 2D electron gas in a strong magnetic field, the Hall conductance is

$$
\sigma_{xy} = \nu\,\frac{e^2}{h},\qquad \nu \in \mathbb{Z},
$$

where $\nu$ is a **Chern number**, the integral of the Berry curvature over the Brillouin zone:

$$
\nu = \frac{1}{2\pi}\int_{BZ} \mathcal{F}\, d^2k .
$$

That integral of a curvature over a closed surface **must** be an integer (Gauss–Bonnet / Chern–Weil), which is why the effect is robust. Thouless, Kohmoto, Nightingale and den Nijs (TKNN, 1982) made this connection. Thouless, Haldane and Kosterlitz shared the 2016 Nobel Prize for topological phases. Today, **topological insulators** (conducting on the surface, insulating inside) are an active field, and **skyrmions** (tiny topological whirls in magnets) are studied for data storage.

### Kelvin's vortex atoms (1867)

Lord Kelvin, inspired by smoke rings, proposed that **atoms are knotted vortices in the ether**, with different knots making different elements. His collaborator P. G. Tait began tabulating knots to build a "periodic table of knots." The theory was wrong: there's no ether, and atomic structure comes from quantum mechanics. But Tait's tables **founded mathematical knot theory**, which now appears in DNA biology (enzymes that untangle DNA), quantum field theory (Witten's work on the Jones polynomial, 1989), and topological quantum computing.

## Where the original notes went too far

- ✅ "Stable structures correspond to phase closing on itself, $\oint \mathbf{k}\cdot d\mathbf{s}=2\pi n$": **this is real physics** (Bohr–Sommerfeld quantization; Berry phase; flux quantization in superconductors).
- ❌ "Lead and gold are the same light tied in different knots; re-tie them with an interference mask": **not supported.** Elements differ by the number of protons in the nucleus. Changing that requires nuclear reactions (MeV energies). Transmutation is real but happens in reactors and accelerators, not with acoustic masks.
- ❌ "$E=mc^2$ comes from two rotations at speed $c$, $c\times c=c^2$": **not how it works.** $c^2$ arises from the geometry of spacetime (Lorentz invariance of the energy–momentum four-vector, $E^2=(pc)^2+(mc^2)^2$).
- ❌ "The Hodge Conjecture proves…": the Hodge Conjecture is **unproven**. It's one of the seven Clay Millennium Prize Problems, with a $1,000,000 prize still unclaimed.
- 🟡 **Quarks:** the notes said quarks can't be isolated because they're "unclosed bends." Quark confinement is real. The actual mechanism (color flux tubes that snap into new quark–antiquark pairs when stretched) is part of QCD, and proving it rigorously is *another* Millennium Prize Problem (Yang–Mills mass gap). The "bent hook" picture is a decent kid-level analogy for flux-tube breaking, but it isn't a theory.

## Try it

- Make a Möbius strip from a paper strip with one half-twist. Cut it along the center line. Then make one with two half-twists and cut that.
- Tie an overhand knot in a rope and try to remove it without passing an end through. You can't.
- See [experiments/E003-vortex-rings.md](../../experiments/E003-vortex-rings.md) to make stable smoke rings, which are Kelvin's inspiration.

## Read more

- D. J. Thouless et al., "Quantized Hall Conductance in a Two-Dimensional Periodic Potential," *Phys. Rev. Lett.* 49, 405 (1982).
- Nobel Prize in Physics 2016: popular science background, nobelprize.org.
- D. Kleckner & W. T. M. Irvine, "Creation and dynamics of knotted vortices," *Nature Physics* 9, 253 (2013).
- Colin Adams, *The Knot Book* (1994).

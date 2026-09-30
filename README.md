# Rise of Geometry 🔺

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/python-3.8%2B-blue.svg)](tools/)
[![tools](https://github.com/utahisnotastate/RiseOfGeometry/actions/workflows/tools.yml/badge.svg)](https://github.com/utahisnotastate/RiseOfGeometry/actions/workflows/tools.yml)
[![Claims audited](https://img.shields.io/badge/claims-audited-brightgreen.svg)](docs/claims/ledger.md)

> **Shape is not decoration. It's the grammar of physics.** Symmetry explains conservation laws, curvature is gravity, twisting is force, and topology is why nature counts in whole numbers.

This repository takes the popular idea of "sacred geometry" and keeps **only what survives contact with evidence**. The result is more remarkable than the mythology: nearly every deep law of physics discovered in the last century turned out to be a statement about geometry.

Every idea here is labeled ✅ **established**, 🟡 **open**, 📜 **historical**, or ❌ **not supported**, and bold claims come with [experiments you can run](experiments/) and [scripts that reproduce every number](tools/).

---

## ⚡ TL;DR, for impatient people

1. **Conservation laws are symmetries.** Energy is conserved *because* physics doesn't change over time. Momentum is conserved *because* space is the same everywhere. (Noether, 1918.) ✅
2. **Gravity isn't a pull. It's curved spacetime.** Your phone's GPS corrects for it every day. ✅
3. **Every force is geometry.** Electromagnetism and the nuclear forces are the "curvature" of hidden internal spaces. Physicists and mathematicians discovered the same math independently. ✅
4. **Shape picks the notes.** A boundary decides which vibrations exist, from drums to atoms to the vacuum itself (the Casimir effect). ✅
5. **The golden ratio is real, but not magic.** It's the "most irrational" number, which is why sunflowers use it to pack seeds. Most other φ claims (Parthenon, DNA, galaxies) don't hold up. ✅ / ❌
6. **Nature has a short list of allowed shapes.** Only five Platonic solids exist. Viruses use the icosahedron. Crystals can't have 5-fold symmetry, and when a material with it was found anyway, it won a Nobel Prize. ✅
7. **Topology makes nature exact.** Some material properties are whole numbers that can't drift. They're precise enough to define the kilogram. ✅
8. **Information lives on surfaces.** The most information a region can hold depends on its area, not its volume. This is the holographic principle. ✅ / 🟡
9. **Empty space is physics' biggest embarrassment.** Theory overestimates vacuum energy by a factor of about 10¹²³. Nobody knows why. 🟡
10. **Can geometry replace physics?** It keeps absorbing more of it, and cutting-edge work suggests spacetime itself may emerge from deeper geometry. But geometry alone can't pick which universe we're in. You still have to measure. 🟡

**And what doesn't survive:** free energy from shapes, reactionless drives, minds linked through "scalar waves," drawings that act like circuits, and anything that breaks conservation of energy or the second law of thermodynamics. Each of those claims is logged, with reasons, in the [claims ledger](docs/claims/ledger.md).

---

## Start here by role

| You are… | Start with |
|---|---|
| 🧒 **A curious kid** (or a busy adult) | [docs/for-kids/](docs/for-kids/README.md) |
| 📚 **A student or general reader** | [Concept 01](docs/concepts/01-symmetry-is-conservation.md) and keep going in order |
| 🔬 **A scientist or skeptic** | [The claims ledger](docs/claims/ledger.md): every claim, every label, every reason |
| 🛠️ **A builder or teacher** | [experiments/](experiments/): household demos and null-test protocols |
| 💻 **A programmer** | [tools/](tools/): standard-library Python that reproduces every number |
| 🤔 **Here for "can geometry replace physics?"** | [Concept 13](docs/concepts/13-can-geometry-replace-physics.md) |

---

## The 13 concepts

Each page follows the same layout: **what everyone wishes they'd noticed sooner → explain it to a kid → examples you already know → the grown-up math → where the original claims went too far → try it yourself → further reading.**

| # | Concept | The big idea in one line | Status |
|---|---|---|---|
| 01 | [Symmetry is conservation](docs/concepts/01-symmetry-is-conservation.md) | Every conservation law is a symmetry in disguise | ✅ |
| 02 | [Gravity is shape](docs/concepts/02-gravity-is-shape.md) | Falling is going straight through curved spacetime | ✅ / 🟡 Mach |
| 03 | [Every force is a twist](docs/concepts/03-forces-are-connections.md) | Forces are the curvature of hidden internal spaces | ✅ |
| 04 | [Shape picks the notes](docs/concepts/04-shape-picks-the-notes.md) | Boundaries select vibrations, even in the vacuum | ✅ |
| 05 | [The golden ratio, honestly](docs/concepts/05-the-golden-ratio-honestly.md) | φ is the most irrational number; that's its only superpower | ✅ / ❌ myths |
| 06 | [The allowed shapes](docs/concepts/06-the-allowed-shapes.md) | Math limits which shapes can exist; nature uses them all | ✅ |
| 07 | [Topology and whole numbers](docs/concepts/07-topology-knots-and-whole-numbers.md) | You can't have half a hole, so some physics is exact | ✅ |
| 08 | [Vortices and tori](docs/concepts/08-vortices-and-tori.md) | Spin plus a donut shape equals stability | ✅ / ❌ free energy |
| 09 | [Waves that run backward](docs/concepts/09-waves-that-run-backward.md) | Time-reversal mirrors and legal faster-than-light phases | ✅ |
| 10 | [Information lives on surfaces](docs/concepts/10-information-lives-on-surfaces.md) | Capacity scales with area, from black holes to brain folds | ✅ / 🟡 |
| 11 | [The vacuum](docs/concepts/11-the-vacuum.md) | Empty space jiggles, and we're wrong about it by 10¹²³ | ✅ / 🟡 |
| 12 | [Boundaries, logic, and computing](docs/concepts/12-boundaries-logic-and-computing.md) | All logic from one line; only forgetting must cost energy | ✅ |
| 13 | [Can geometry replace physics?](docs/concepts/13-can-geometry-replace-physics.md) | It's the grammar of physics, but nature picks the sentence | 🟡 |

Also: [Glossary](docs/glossary.md)

---

## Things everyone wishes they'd caught sooner

These are real, documented, and still surprising:

- **Energy conservation was never a separate law.** It's what "physics works the same tomorrow" means. ([01](docs/concepts/01-symmetry-is-conservation.md))
- **Physicists and mathematicians spent decades building the same theory without realizing it.** Gauge fields are fiber-bundle connections. When Yang found out, he was stunned. ([03](docs/concepts/03-forces-are-connections.md))
- **An electron can feel a magnetic field it never enters.** (Aharonov–Bohm, confirmed 1986.) ([03](docs/concepts/03-forces-are-connections.md))
- **Shechtman was mocked for years for seeing a "forbidden" crystal.** He won the Nobel Prize in 2011. ([06](docs/concepts/06-the-allowed-shapes.md))
- **Kelvin's wrong idea that atoms are knots founded all of knot theory**, now used in DNA biology and quantum computing. ([07](docs/concepts/07-topology-knots-and-whole-numbers.md))
- **Doctors focus sound through the body with "time-reversed" waves.** ([09](docs/concepts/09-waves-that-run-backward.md))
- **Your computer uses about a billion times more energy per operation than physics requires.** ([12](docs/concepts/12-boundaries-logic-and-computing.md))
- **Particle collisions can be computed as the volume of a geometric shape** (the amplituhedron) instead of thousands of diagrams. ([13](docs/concepts/13-can-geometry-replace-physics.md))
- **Kepler's Platonic-solid solar system was wrong, and trying to prove it led him to the laws of planetary motion.** Testing a beautiful wrong idea honestly is how science wins. ([06](docs/concepts/06-the-allowed-shapes.md))

---

## Try it in 30 seconds

```bash
git clone https://github.com/utahisnotastate/RiseOfGeometry.git
cd RiseOfGeometry
python tools/big_numbers.py      # the 10^42 coincidence, Planck density, the 10^123 problem
python tools/golden_angle.py     # why sunflowers use 137.5°
python tools/noether_orbit.py    # watch symmetry create a conservation law
python tools/chladni.py 3 5      # draw a Chladni figure in your terminal
```

No dependencies beyond Python 3.

---

## Where this came from, and how it was cleaned up

This project began as a set of speculative notes framed as "future disclosures" about sacred geometry. Those notes mixed genuine physics (Noether, Casimir, KAM, Bekenstein, Laws of Form, phase conjugation) with material that has no evidential basis (psychotronics, scalar-wave weapons, free-energy tori, "timeline" sourcing).

The cleanup followed three rules:

1. **Keep every real result**, explain it accurately, and give it proper references.
2. **Log every unsupported claim** in the [ledger](docs/claims/ledger.md), with its status and the reason, so nothing is hidden and anyone can challenge a label.
3. **Remove narrative framing entirely.** A claim's source story doesn't make it more or less true. Only evidence does.

What remained is a story that doesn't need embellishment: **the rise of geometry from Euclid's five solids to the shape of spacetime itself.**

---

## Contributing

Corrections, clearer explanations, experiment data, and evidence-backed label changes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Use it, teach with it, remix it.

## Related projects

- [FallOfPhysics](https://github.com/utahisnotastate/FallOfPhysics)
- [ufwwaragainstthemitochondria](https://github.com/utahisnotastate/ufwwaragainstthemitochondria)
- [ufwwaragainstearthscience](https://github.com/utahisnotastate/ufwwaragainstearthscience)

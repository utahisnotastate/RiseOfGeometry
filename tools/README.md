# Tools

Small, dependency-free Python 3 scripts. Each one reproduces numbers or effects quoted in the docs, so you never have to take a figure on trust.

| Script | What it shows | Used in |
|---|---|---|
| `big_numbers.py` | Z₀, the 10⁴² ratio, Planck density, the 10¹²³ vacuum mismatch, Casimir pressure, Schumann modes, computation limits | [11](../docs/concepts/11-the-vacuum.md), [ledger](../docs/claims/ledger.md) |
| `most_irrational.py` | Continued fractions; why φ is the hardest number to approximate | [05](../docs/concepts/05-the-golden-ratio-honestly.md) |
| `golden_angle.py` | Sunflower packing quality vs. turning angle (`--svg` for pictures) | [05](../docs/concepts/05-the-golden-ratio-honestly.md), [E002](../experiments/E002-count-the-spirals.md) |
| `chladni.py` | Chladni figures for a square plate (`--pgm` for an image) | [04](../docs/concepts/04-shape-picks-the-notes.md), [E001](../experiments/E001-chladni-plate.md) |
| `noether_orbit.py` | Symmetry → conservation, shown by simulation | [01](../docs/concepts/01-symmetry-is-conservation.md) |
| `allowed_symmetries.py` | Crystallographic restriction; why only five Platonic solids | [06](../docs/concepts/06-the-allowed-shapes.md), [E004](../experiments/E004-platonic-solids.md) |
| `phase_velocity.py` | Phase × group velocity = c² in waveguides and matter waves | [09](../docs/concepts/09-waves-that-run-backward.md) |

```bash
python tools/big_numbers.py
```
(On Windows, use `py` if `python` isn't on your PATH.)

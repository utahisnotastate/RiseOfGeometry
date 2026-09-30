# E001 · Chladni Plate: Let the Shape Draw the Picture

**Shows:** A boundary plus a frequency selects a standing-wave pattern. ([Concept 04](../docs/concepts/04-shape-picks-the-notes.md))
**Status of the effect:** ✅ Established (Chladni, 1787).

## You'll need
- A thin, stiff metal plate (a baking sheet, cookie tin lid, or 20–30 cm square of 1 mm aluminum)
- Fine salt, sugar, or dry sand
- **Option A:** a violin or cello bow with rosin
- **Option B:** a small speaker or "tactile transducer" (bass shaker), a cheap amplifier, and a free tone-generator app or website

## Method
1. Fix the plate at its **center** (bolt it to the speaker cone or a post, or pinch it with a clamp).
2. Sprinkle a thin, even layer of salt.
3. **Bow method:** draw the bow firmly down the edge. Touching a finger to another point on the edge selects different modes.
   **Speaker method:** sweep slowly from about 100 Hz to 3000 Hz. Stop when the salt suddenly organizes into lines.
4. Photograph each pattern and note its frequency.

## What to look for
- Salt collects on **nodal lines**, where the plate doesn't move.
- Higher frequencies give more lines and finer patterns.
- **Change the plate's shape** (square → circle → triangle) and the whole family of patterns changes. That's the point: *shape selects the notes.*

## Compare with theory
```bash
python tools/chladni.py 2 3
python tools/chladni.py 3 5
```
The idealized square-plate formula won't match your plate exactly, because real plates are clamped at the center and have a finite thickness. But the family resemblance is clear.

## Safety
Keep speaker volume moderate. Wear ear protection if you run it loud for long.

## Going further
- Use a **circular** plate and plot the frequencies against the pattern. With $m$ straight (diameter) lines and $n$ rings, they roughly follow $f \propto (m+2n)^2$ (Chladni's law).
- Try a **Rubens tube** or a guitar body.

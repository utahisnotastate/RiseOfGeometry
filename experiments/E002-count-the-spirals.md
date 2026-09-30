# E002 · Count the Spirals

**Shows:** Plants place seeds and leaves near the golden angle, producing Fibonacci spiral counts. ([Concept 05](../docs/concepts/05-the-golden-ratio-honestly.md))
**Status of the effect:** ✅ Established as a strong tendency (about 80% of sunflower heads in the largest survey).

## You'll need
- Pinecones, a sunflower head, a pineapple, a daisy, a cauliflower or Romanesco broccoli
- A washable marker or pins, and a notebook

## Method
1. Pick a spiral running **clockwise** from the center outward. Mark it. Count how many parallel clockwise spirals there are.
2. Do the same for **counter-clockwise** spirals.
3. Record both numbers for every specimen.

## Prediction (write yours down before counting!)
If phyllotaxis follows the golden angle, the two counts should usually be **neighboring Fibonacci numbers**: 3 & 5, 5 & 8, 8 & 13, 13 & 21, 21 & 34, 34 & 55, 55 & 89.

## What honest results look like
- Many specimens will fit. **Some won't.** The 2016 Manchester study of 657 sunflowers found about 1 in 5 didn't show Fibonacci counts. Record those too. They're part of the real answer.
- Pinecones typically give 5 & 8 or 8 & 13. Pineapples typically give 8 & 13.

## Compare with a simulation
```bash
python tools/golden_angle.py --svg
```
Open `sunflower_137.508.svg` and count its spirals the same way. Then open `sunflower_137.000.svg`. Half a degree off, and the pattern changes.

## Going further
Contribute counts to a citizen science project, or share your data table in a pull request as `experiments/data/E002-<yourname>.csv`.

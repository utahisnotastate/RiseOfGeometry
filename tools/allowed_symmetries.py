"""The crystallographic restriction: why crystals can't have 5-fold symmetry
(and why quasicrystals were such a shock).

A lattice rotation written in lattice coordinates must be a matrix of whole
numbers, so its trace 2*cos(360/n) has to be a whole number. Only n = 1, 2, 3, 4, 6 pass.

Also lists the five Platonic solids and checks Euler's formula V - E + F = 2.

Run:  python tools/allowed_symmetries.py
"""
import math

print("n-fold rotation   trace 2cos(360/n)   allowed in a repeating crystal?")
for n in range(1, 13):
    t = 2 * math.cos(2 * math.pi / n)
    ok = abs(t - round(t)) < 1e-9
    print(f"{n:>6}            {t:>8.4f}            {'yes' if ok else 'no'}")

print("\nPlatonic solids (the only five convex shapes with identical regular faces and corners)")
solids = [("tetrahedron", 4, 6, 4), ("cube", 8, 12, 6), ("octahedron", 6, 12, 8),
          ("dodecahedron", 20, 30, 12), ("icosahedron", 12, 30, 20)]
print(f"{'solid':<14}{'V':>4}{'E':>5}{'F':>5}   V - E + F")
for name, v, e, f in solids:
    print(f"{name:<14}{v:>4}{e:>5}{f:>5}   {v - e + f}")

print("\nWhy only five: with p-sided faces, q meeting at each corner, the angles must")
print("add to less than 360 degrees, which forces (p-2)(q-2) < 4. Solutions (p,q):")
print("  ", [(p, q) for p in range(3, 10) for q in range(3, 10) if (p - 2) * (q - 2) < 4])

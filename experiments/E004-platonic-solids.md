# E004 · Build the Five Platonic Solids

**Shows:** Exactly five convex regular polyhedra exist; Euler's formula $V-E+F=2$. ([Concept 06](../docs/concepts/06-the-allowed-shapes.md))
**Status:** ✅ Proven (Euclid, *Elements* Book XIII; Euler 1758).

## You'll need
- Toothpicks and gumdrops (or mini marshmallows), **or** printed paper nets, scissors, and tape

## Method
1. Build a tetrahedron (4 triangles), octahedron (8 triangles), icosahedron (20 triangles), cube (6 squares), and dodecahedron (12 pentagons).
2. For each, count vertices $V$, edges $E$, and faces $F$. Check $V - E + F$.
3. **The impossibility test:** try to build a solid with **6 triangles at every corner**. It lies flat. Try **4 squares** at a corner: flat again. Try **3 hexagons**: flat. That's why there are only five.

## Discussion questions
- Which solid has the most volume for a given edge length? (Icosahedron among the triangle ones.) Why might viruses prefer it?
- The cube and octahedron have the same number of edges, and so do the dodecahedron and icosahedron. Why? (They're **duals**: swap faces for vertices.)

## Check with code
```bash
python tools/allowed_symmetries.py
```

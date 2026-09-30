"""Sunflower seed packing: why plants use the golden angle.

Places N seeds one after another, each turned by a fixed angle from the last
(Vogel's 1979 model: radius ~ sqrt(n)). Then measures how evenly the seeds
fill the disc. The golden angle wins; nearby "nice" angles leave gaps or spokes.

Run:  python tools/golden_angle.py            (prints a score table)
      python tools/golden_angle.py --svg      (also writes sunflower_*.svg)
"""
import math
import sys

N = 600


def seeds(angle_deg, n=N):
    a = math.radians(angle_deg)
    return [(math.sqrt(k) * math.cos(k * a), math.sqrt(k) * math.sin(k * a)) for k in range(1, n + 1)]


def evenness(pts):
    """Smallest nearest-neighbour distance divided by the mean one.
    1.0 = perfectly even spacing, near 0 = seeds crowding together."""
    nn = []
    for i, (x, y) in enumerate(pts):
        best = min((x - u) ** 2 + (y - v) ** 2 for j, (u, v) in enumerate(pts) if j != i)
        nn.append(math.sqrt(best))
    return min(nn) / (sum(nn) / len(nn))


def write_svg(angle_deg, path):
    pts = seeds(angle_deg)
    r = math.sqrt(N) + 1
    dots = "".join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.45"/>' for x, y in pts)
    with open(path, "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-r} {-r} {2*r} {2*r}" '
                f'width="400" height="400"><g fill="#c47f00">{dots}</g></svg>')


GOLDEN = 360 * (1 - 2 / (1 + math.sqrt(5)))
angles = [("90 (quarter turn)", 90.0), ("120 (third turn)", 120.0), ("135", 135.0),
          ("137.0", 137.0), ("137.508 GOLDEN", GOLDEN), ("138.0", 138.0), ("144 (2/5 turn)", 144.0)]

print(f"{'angle (degrees)':<22} evenness (1.0 = perfect)")
for label, ang in angles:
    print(f"{label:<22} {evenness(seeds(ang)):.3f}")
    if "--svg" in sys.argv:
        write_svg(ang, f"sunflower_{ang:.3f}.svg")
if "--svg" in sys.argv:
    print("\nWrote sunflower_*.svg - open them in a browser to see spokes vs. a perfect sunflower.")

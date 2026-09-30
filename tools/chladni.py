"""Chladni figures: the shape of a plate picks its patterns.

For a square plate, a good approximation to the nodal lines (where sand
collects) is where
    cos(n pi x) cos(m pi y) - cos(m pi x) cos(n pi y) = 0.
Different (n, m) pairs are different notes.

Run:  python tools/chladni.py 3 5            (ASCII preview in the terminal)
      python tools/chladni.py 3 5 --pgm      (also writes chladni_3_5.pgm image)
"""
import math
import sys


def field(n, m, x, y):
    return (math.cos(n * math.pi * x) * math.cos(m * math.pi * y)
            - math.cos(m * math.pi * x) * math.cos(n * math.pi * y))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n, m = (int(args[0]), int(args[1])) if len(args) == 2 else (3, 5)
    if n == m:
        sys.exit("n and m must differ (n == m gives a flat plate).")

    w, h = 72, 36
    print(f"Chladni pattern (n={n}, m={m}): '#' = sand lines (nodes)\n")
    for j in range(h):
        y = j / (h - 1)
        print("".join("#" if abs(field(n, m, i / (w - 1), y)) < 0.12 else " " for i in range(w)))

    if "--pgm" in sys.argv:
        size = 400
        path = f"chladni_{n}_{m}.pgm"
        with open(path, "w") as f:
            f.write(f"P2\n{size} {size}\n255\n")
            for j in range(size):
                y = j / (size - 1)
                f.write(" ".join("0" if abs(field(n, m, i / (size - 1), y)) < 0.04 else "255"
                                 for i in range(size)) + "\n")
        print(f"\nWrote {path}")


if __name__ == "__main__":
    main()

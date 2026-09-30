"""Noether's theorem you can watch: symmetry in, conservation out.

Simulates a planet in two force fields:
  1. a perfectly round (rotationally symmetric) field  -> angular momentum is conserved
  2. the same field squashed into an oval shape        -> angular momentum is NOT conserved
Energy is conserved in both, because neither field changes with time
(time symmetry -> energy conservation).

Run:  python tools/noether_orbit.py
"""
import math


def accel(x, y, squash):
    # Potential V = -1 / sqrt(x^2 + (squash*y)^2). squash = 1 is perfectly round.
    r3 = (x * x + (squash * y) ** 2) ** 1.5
    return -x / r3, -(squash ** 2) * y / r3


def energy(x, y, vx, vy, squash):
    return 0.5 * (vx * vx + vy * vy) - 1 / math.sqrt(x * x + (squash * y) ** 2)


def run(squash, steps=200_000, dt=1e-4):
    x, y, vx, vy = 1.0, 0.0, 0.0, 1.1
    L0, E0 = x * vy - y * vx, energy(x, y, vx, vy, squash)
    maxdL = maxdE = 0.0
    ax, ay = accel(x, y, squash)
    for _ in range(steps):  # velocity Verlet: a standard, energy-friendly integrator
        vx += 0.5 * dt * ax
        vy += 0.5 * dt * ay
        x += dt * vx
        y += dt * vy
        ax, ay = accel(x, y, squash)
        vx += 0.5 * dt * ax
        vy += 0.5 * dt * ay
        maxdL = max(maxdL, abs(x * vy - y * vx - L0))
        maxdE = max(maxdE, abs(energy(x, y, vx, vy, squash) - E0))
    return maxdL, maxdE


for label, s in (("round field (symmetric)", 1.0), ("oval field (symmetry broken)", 1.3)):
    dL, dE = run(s)
    print(f"{label:<30} max drift in angular momentum: {dL:.2e}   max drift in energy: {dE:.2e}")
print("\nRound field: both stay fixed. Oval field: energy stays fixed, angular momentum wanders.")
print("Break a symmetry and you lose exactly the conservation law it was paying for.")

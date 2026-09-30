"""Phase velocity vs. group velocity: the legal way to 'beat' light.

In a metal waveguide (and for de Broglie matter waves), the phase velocity is
faster than light while the group velocity - the speed of energy and
information - is slower, with  v_phase * v_group = c^2  exactly.

Run:  python tools/phase_velocity.py
"""
import math

c = 2.99792458e8
f_cut = 6.56e9  # cutoff of a standard WR-90 waveguide, Hz

print("Rectangular waveguide, TE10 mode (cutoff 6.56 GHz)")
print(f"{'frequency (GHz)':>16} {'v_phase / c':>12} {'v_group / c':>12} {'product / c^2':>14}")
for f in (6.7e9, 7e9, 8e9, 10e9, 15e9, 40e9):
    s = math.sqrt(1 - (f_cut / f) ** 2)
    vp, vg = c / s, c * s
    print(f"{f / 1e9:>16.1f} {vp / c:>12.3f} {vg / c:>12.3f} {vp * vg / c**2:>14.6f}")

print("\nElectron matter wave (de Broglie)")
print(f"{'speed v / c':>12} {'v_phase / c':>12}")
for beta in (0.001, 0.01, 0.1, 0.5, 0.9, 0.99):
    print(f"{beta:>12} {1 / beta:>12.1f}")
print("\nThe phase races ahead, but no signal ever does. Nothing here breaks relativity.")

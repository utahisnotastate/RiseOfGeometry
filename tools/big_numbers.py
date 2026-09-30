"""Compute the famous "big numbers" of physics from CODATA-style constants.

Every number quoted in docs/concepts/11-the-vacuum.md and docs/claims/ledger.md
comes from this script, so anyone can check them.

Run:  python tools/big_numbers.py
"""
import math

# Constants (SI, CODATA 2018 values, rounded)
c = 2.99792458e8          # speed of light, m/s
hbar = 1.054571817e-34    # reduced Planck constant, J s
G = 6.67430e-11           # gravitational constant, m^3 kg^-1 s^-2
e = 1.602176634e-19       # elementary charge, C
eps0 = 8.8541878128e-12   # vacuum permittivity, F/m
mu0 = 1.25663706212e-6    # vacuum permeability, N/A^2
m_e = 9.1093837015e-31    # electron mass, kg
m_p = 1.67262192369e-27   # proton mass, kg
r_e = 2.8179403262e-15    # classical electron radius, m
R_earth = 6.371e6         # mean Earth radius, m
H0 = 67.4e3 / 3.0857e22   # Hubble constant (Planck 2018), 1/s
rho_lambda = 5.8e-27      # observed dark-energy density, kg/m^3 (approx.)


def row(label, value, unit=""):
    print(f"  {label:<52} {value:>12.4g} {unit}")


print("\n1. Vacuum impedance")
row("Z0 = sqrt(mu0/eps0)", math.sqrt(mu0 / eps0), "ohm")

print("\n2. The 10^42 coincidence (Weyl, Eddington, Dirac)")
k = 1 / (4 * math.pi * eps0)
row("Electric / gravitational force, two electrons", k * e**2 / (G * m_e**2))
row("Electric / gravitational force, electron + proton", k * e**2 / (G * m_e * m_p))
hubble_radius = c / H0
row("Hubble radius c/H0", hubble_radius, "m")
row("Hubble radius / classical electron radius", hubble_radius / r_e)

print("\n3. Planck scale")
l_p = math.sqrt(hbar * G / c**3)
t_p = l_p / c
rho_p = c**5 / (hbar * G**2)
row("Planck length", l_p, "m")
row("Planck time", t_p, "s")
row("Planck density", rho_p, "kg/m^3")
row("Planck density", rho_p * 1e-3, "g/cm^3")
row("Nuclear density (approx.)", 2.3e17 * 1e-3, "g/cm^3")

print("\n4. The cosmological-constant problem")
row("Observed dark-energy density", rho_lambda, "kg/m^3")
row("Observed / naive Planck-scale estimate", rho_lambda / rho_p)
print(f"  -> mismatch of about 10^{math.log10(rho_p / rho_lambda):.0f}")

print("\n5. Casimir pressure between ideal parallel plates, P = pi^2 hbar c / (240 a^4)")
for a in (1e-6, 1e-7, 1e-8):
    row(f"gap a = {a:.0e} m", math.pi**2 * hbar * c / (240 * a**4), "Pa")

print("\n6. Schumann resonances")
f0 = c / (2 * math.pi * R_earth)
measured = [7.83, 14.3, 20.8, 27.3, 33.8]
print("  n   ideal lossless cavity (Hz)   measured (Hz)")
for n in range(1, 6):
    print(f"  {n}   {f0 * math.sqrt(n * (n + 1)):>10.2f}                {measured[n - 1]:>8.2f}")
print("  (Real values are lower because the Earth-ionosphere cavity is lossy.)")

print("\n7. Ultimate speed limit on computation (Margolus-Levitin), 1 kg")
row("Max operations per second = 2E/(pi hbar), E = mc^2", 2 * (1 * c**2) / (math.pi * hbar), "ops/s")

print("\n8. Sanity check on an 'EEG at 8.1e20 Hz' claim")
f = 8.1e20
h = 2 * math.pi * hbar
row("Wavelength c/f", c / f, "m")
row("Photon energy hf", h * f / 1.602176634e-13, "MeV")
print("  -> that is gamma radiation, not a brain rhythm (EEG is measured below ~1 kHz).")
print()

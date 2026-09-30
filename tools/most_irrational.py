"""Why the golden ratio is the "most irrational" number.

A number is hard to approximate with fractions when its continued fraction has
small terms. The golden ratio phi = [1; 1, 1, 1, ...] has the smallest possible
terms, so it is the worst-approximated number of all (Hurwitz's theorem).
That is the real reason it shows up in sunflowers and in the KAM theorem.

Run:  python tools/most_irrational.py
"""
import math

PHI = (1 + math.sqrt(5)) / 2


def continued_fraction(x, terms=10):
    out = []
    for _ in range(terms):
        a = math.floor(x)
        out.append(a)
        frac = x - a
        if frac < 1e-12:
            break
        x = 1 / frac
    return out


def convergents(cf):
    """Yield successive best rational approximations p/q."""
    p0, q0, p1, q1 = 1, 0, cf[0], 1
    yield p1, q1
    for a in cf[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        yield p1, q1


def report(name, x):
    cf = continued_fraction(x, 8)
    print(f"\n{name} = {x:.10f}")
    print(f"  continued fraction: {cf}")
    print("  best fractions p/q and how good they are (q^2 * error; bigger = harder to approximate):")
    for p, q in list(convergents(cf))[1:6]:
        err = abs(x - p / q)
        print(f"    {p:>6}/{q:<6} error {err:.2e}   q^2*error {q * q * err:.3f}")


report("phi (golden ratio)", PHI)
report("sqrt(2)", math.sqrt(2))
report("pi", math.pi)
report("e", math.e)

print(f"\nHurwitz limit 1/sqrt(5) = {1 / math.sqrt(5):.3f}: phi's q^2*error approaches this, the worst possible.")
print(f"Golden angle = 360 * (1 - 1/phi) = {360 * (1 - 1 / PHI):.3f} degrees")

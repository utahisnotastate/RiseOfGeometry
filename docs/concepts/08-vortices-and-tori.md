# 08 · Vortices and Tori: Nature's Favorite Way to Hold Things Together

> A smoke ring holds its shape across a room. A donut-shaped magnet keeps its field inside. Rotation plus the right shape equals stability.

**Status:** ✅ Established (vortex rings, toroidal confinement, tokamaks). ❌ Not supported: toroidal coils that produce free energy or cancel back-EMF.

---

## What everyone wishes they'd noticed sooner

A torus (a donut shape) is the simplest shape where something can flow **around forever without hitting an end**. That's why it shows up whenever nature or engineers need to *keep* something:

- A **smoke ring** carries its spin across a room without falling apart.
- A **toroidal transformer** keeps almost all its magnetic field inside the core, with less leakage and hum than a square one.
- **Fusion reactors** (tokamaks) use a torus of magnetic field to hold plasma at 150 million °C.
- A **particle accelerator** like the LHC is a ring for the same reason.

The shape does real work: it removes the "ends" where things leak, collide, or reflect.

## Explain it to a kid

Try emptying a big bottle of water by turning it upside down. It glugs and splashes because air and water fight over the neck. Now swirl it first. A whirlpool forms, air goes up the middle, water spirals down the walls, and it empties much faster.

**The swirl didn't add power. It organized the flow so the two things stopped fighting.** That's what vortices and donut shapes are good at: letting things flow smoothly without bumping into each other.

## Examples you already know

- **Swirling a bottle** really does empty it faster. It's a fun race to try.
- **Dolphins blow bubble rings** and play with them.
- **Tornadoes and hurricanes** are vortices that can hold together for days.
- **Vortex cannons** (a box with a hole) shoot air rings that can blow out a candle across a room.
- **Your heart** creates vortex rings in the left ventricle each beat, which helps blood flow efficiently. This is actively studied in cardiology (Gharib and others).
- **Toroidal inductors** in power supplies and audio gear are donut-shaped because the field stays inside the core.

## The grown-up version

**Vortex rings** are stable because of Kelvin's circulation theorem. In an ideal fluid, the circulation $\Gamma=\oint \mathbf{v}\cdot d\boldsymbol\ell$ around a loop moving with the fluid is constant. The ring moves at a speed set by its own circulation and radius:

$$
U \approx \frac{\Gamma}{4\pi R}\left[\ln\frac{8R}{a}-\frac14\right].
$$

**Toroidal confinement.** For an ideal toroidal solenoid, Ampère's law gives $B = \mu_0 N I / (2\pi r)$ inside the core and essentially $B=0$ outside. The field lines close on themselves with no ends.

**Tokamaks** add a twist (a poloidal field) so charged particles spiral around the torus. Pure toroidal fields let particles drift out. The twist, measured by the "safety factor" $q$, is a geometric design parameter, and choosing it well is much of the art of fusion engineering. ITER, under construction in France, is the largest tokamak ever built.

## Where the original notes went too far

- ✅ "Toroidal geometry is efficient and confining": **true**.
- ❌ "Asymmetric toroidal vortices draw energy from the vacuum": **not supported.** Every toroidal device ever measured obeys conservation of energy.
- ❌ "Engineers burn fuel fighting back-EMF because of bad circuit shape": back-EMF is **Lenz's law**, which is conservation of energy in electrical form. If a changing current *didn't* push back, you could build a perpetual motion machine. Shape can change how much field leaks out, not whether energy is conserved.
- ❌ "Inomata's complex thermodynamics lets entropy decrease with no cost": Shiuji Inomata was a real researcher at Japan's Electrotechnical Laboratory, but his "virtual entropy" framework isn't accepted physics and has no experimental confirmation. The second law of thermodynamics has never been observed to fail for a macroscopic system.

If you want to test a free-energy torus claim yourself, [experiments/E006-energy-audit.md](../../experiments/E006-energy-audit.md) shows how to measure input and output power properly. This is where nearly every claim fails: peak readings instead of true RMS power, or ignoring the phase between voltage and current.

## Try it

- **Vortex cannon:** tape plastic over the open end of a cardboard box, cut a 5 cm hole in the other end, add smoke or fog, and tap the plastic. See [experiments/E003-vortex-rings.md](../../experiments/E003-vortex-rings.md).
- **Bottle race:** time two identical bottles emptying, one swirled and one not.

## Read more

- P. G. Saffman, *Vortex Dynamics* (1992).
- M. Gharib et al., "Optimal vortex formation as an index of cardiac health," *PNAS* 103, 6305 (2006).
- ITER Organization, iter.org, for how a torus holds a star.

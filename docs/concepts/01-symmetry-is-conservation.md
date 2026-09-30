# 01 · Symmetry *Is* Conservation

> Every conservation law in physics is a symmetry of shape wearing a disguise.

**Status:** ✅ Established. Proved by Emmy Noether in 1918 and tested countless times since.

---

## What everyone wishes they'd noticed sooner

For about two hundred years, students memorized conservation of energy, conservation of momentum, and conservation of angular momentum as three separate rules. Then Emmy Noether showed they aren't separate rules at all. Each one is a **geometric symmetry**:

| If the laws of physics don't change when you… | …then this is conserved |
|---|---|
| wait (shift in **time**) | **energy** |
| move (shift in **space**) | **momentum** |
| turn (rotate in **space**) | **angular momentum** |
| rotate the phase of a quantum wave | **electric charge** |

Nobody "invented" conservation of energy. It's what you get automatically from the fact that an experiment done on Tuesday works the same as one done on Wednesday.

## Explain it to a kid

Imagine a merry-go-round that is perfectly round. If you're spinning on it and pull your arms in, you speed up, and nothing can stop you from keeping your spin. Now make the merry-go-round lumpy, with a bump on one side. Every time you pass the bump, you get a little shove, and your spin changes.

**Perfectly round means spin is saved. Lumpy means spin leaks away.** That's the whole theorem. The shape of the world decides what gets saved.

## Examples you already know

- **Ice skater spin.** A skater pulls in her arms and spins faster. Angular momentum is conserved because the ice doesn't care which direction she faces (rotational symmetry).
- **Planets.** Earth sweeps out equal areas in equal times (Kepler's second law). That's angular momentum conservation, which comes from the Sun's gravity pulling the same in every direction.
- **Why a thrown ball follows a parabola.** Horizontal momentum is conserved because space is the same everywhere left to right. Vertical momentum isn't, because "up" and "down" are different near Earth.
- **The expanding universe.** Light stretches and loses energy as the universe expands. Energy isn't conserved in the usual way on cosmic scales, *because the universe isn't the same at all times*. Noether predicts exactly this loophole.

## The grown-up version

For a system described by a Lagrangian $L(q, \dot q, t)$, if a continuous transformation $q \to q + \epsilon\,\delta q$ leaves the action $S=\int L\,dt$ unchanged, then

$$
Q = \frac{\partial L}{\partial \dot q}\,\delta q
\qquad\text{satisfies}\qquad \frac{dQ}{dt}=0 .
$$

- Time translation ⇒ $Q$ = Hamiltonian (energy).
- Spatial translation ⇒ $Q$ = linear momentum.
- Rotation ⇒ $Q$ = angular momentum.
- Global $U(1)$ phase symmetry of a quantum field ⇒ $Q$ = electric charge.

Modern particle physics is organized almost entirely by symmetry groups: $SU(3)\times SU(2)\times U(1)$ for the Standard Model, the Lorentz group for relativity. Choosing the symmetry comes first. The equations follow.

## How this connects to the original notes

The source material said forces are "not primary causal entities" but are secondary to geometry. In a precise sense, that's the true core of this idea: symmetry (geometry) determines which quantities are conserved and which forces are allowed. The notes attached that true core to a lot of invented machinery. It doesn't need any.

## Try it

```bash
python tools/noether_orbit.py
```

This simulates a planet in a round force field and in an oval one. In the round field, angular momentum stays fixed to 14 decimal places. In the oval field it wanders, while energy (which depends on *time* symmetry, not shape) stays fixed in both.

## Read more

- E. Noether, *Invariante Variationsprobleme* (1918). English translation: M. A. Tavel, *Transport Theory and Statistical Physics* 1, 186 (1971).
- Leon Lederman & Christopher Hill, *Symmetry and the Beautiful Universe* (2004). Accessible.
- Feynman, *The Character of Physical Law*, ch. 4 "Symmetry in Physical Law".

# 09 · Waves That Run Backward, and Waves That Outrun Light

> There's a mirror that sends light back exactly the way it came, undoing distortion. And there are wave patterns that move faster than light, legally. Both are real. Neither does what the myths say.

**Status:** ✅ Established (optical phase conjugation, acoustic time-reversal mirrors, superluminal phase velocity). ❌ Not supported: using phase conjugation to reverse aging or disease, or using phase velocity to send signals faster than light.

---

## Part 1: The time-reversal mirror

### What everyone wishes they'd noticed sooner

A normal mirror bounces light like a ball off a wall. A **phase-conjugate mirror** does something stranger. It sends each part of the wave back *exactly along the path it came*, as if the wave were a movie played backward. Shine a laser through a frosted, bumpy piece of glass, bounce it off a phase-conjugate mirror, and when it goes back through the same bumpy glass, **the distortion cancels out** and you get a clean beam again.

Discovered in 1972 by Boris Zel'dovich's group in Moscow, this is used in high-power lasers and, in its acoustic form, in medicine.

### Explain it to a kid

Picture a crowd of kids running out of a room in all directions, bumping around furniture. At a whistle, every kid turns around and walks back **exactly** the way they came, retracing every bump and swerve. They all arrive back at the door at the same moment.

A phase-conjugate mirror does that to a wave. It isn't magic, and it only works while the "kids" still remember their paths. Once the wave has turned into random heat (the kids went home), there's nothing left to rewind.

### Real examples

- **Time-reversal acoustics (Mathias Fink, Paris).** An array of microphones records the sound from a spot in the body, then plays it back time-reversed. The sound refocuses on that exact spot even through bone and tissue. It's studied for **breaking kidney stones**, targeted ultrasound therapy, and underwater communication.
- **Laser engineering.** Phase conjugation corrects distortion in powerful laser amplifiers.
- **Telescopes** use a related trick (adaptive optics) to undo atmospheric blurring of stars.

### The grown-up version

In a medium with third-order nonlinearity $\chi^{(3)}$, two counter-propagating pump beams and a probe $E_p \propto A_p e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}$ generate

$$
E_c \propto A_p^{*}\, e^{-i(\mathbf{k}\cdot\mathbf{r}+\omega t)} ,
$$

a wave with conjugated spatial phase and reversed wavevector. This is **degenerate four-wave mixing**. The reversal is of the *spatial phase*, and only for the *coherent* part of the wave. Thermal (incoherent) energy has no phase to conjugate.

### Where the original notes went too far

- ✅ "A phase-conjugate wave retraces its path through distortions": **true.**
- ❌ "It can reverse entropy, rejuvenate cells, or un-break a mug": **not supported.** Phase conjugation needs a coherent wave and costs pump energy. A broken mug's history has become heat and sound spread through the room, and no device can collect it. This is exactly the second law of thermodynamics.
- ❌ "Antoine Priore's machine cured cancer this way": Priore's 1960s–70s French device got press and some animal studies, but results were never independently replicated and the device has never been validated.

---

## Part 2: Faster than light, legally

### What everyone wishes they'd noticed sooner

Close a pair of giant scissors. The blades move slowly, but the **point where they cross** can zip toward the tips faster than light if the scissors are long enough and nearly closed. Nothing breaks relativity, because that crossing point **isn't a thing**. It carries no message from one end to the other.

Waves have the same split:
- The **phase velocity** (how fast the crests move) can exceed $c$.
- The **group velocity** (how fast energy and information move) never does, in normal conditions.

### Real examples

- **Metal waveguides** (used in radar and microwave ovens): phase velocity > $c$, group velocity < $c$, and their product is exactly $c^2$.
- **De Broglie matter waves.** An electron moving at speed $v$ has a phase velocity of $c^2/v$, faster than light, always. This is textbook quantum mechanics (de Broglie, 1924).
- **A lighthouse beam** sweeping across distant clouds: the spot can move faster than light across the clouds. No signal travels from one cloud to the other.

### The grown-up version

For a relativistic particle, $\omega^2 = c^2k^2 + \omega_0^2$ with $\omega_0 = mc^2/\hbar$. Then

$$
v_g = \frac{d\omega}{dk} = \frac{c^2 k}{\omega} = v, \qquad v_p = \frac{\omega}{k} = \frac{c^2}{v}, \qquad v_p v_g = c^2 .
$$

Information travels with the front of a signal. Sommerfeld and Brillouin (1914) showed the front velocity never exceeds $c$.

### Where the original notes went too far

- ✅ "De Broglie phase velocity is $c^2/v$ and superluminal": **true.**
- ❌ "Therefore every accelerating mass pulses the entire universe instantly and enables non-local data retrieval": **not supported.** Phase velocity carries no information.
- ❌ "Velocities of $c^2$, $c^3$ are dimensional thresholds": $c^2$ has units of m²/s². **It isn't a speed**, so "moving at $c^2$" has no meaning.

## Try it

```bash
python tools/phase_velocity.py
```

- **Scissors demo:** open long scissors (or two rulers pinned together) and close them slowly. Watch how fast the crossing point moves compared to the blades.
- **Wave tank:** ripples in a pan of water show crests moving at a different speed than the group of ripples. Watch a single ripple crest travel through the group.

## Read more

- B. Ya. Zel'dovich et al., *JETP Letters* 15, 109 (1972). (First optical phase conjugation.)
- M. Fink, "Time-reversed acoustics," *Scientific American* (Nov 1999).
- L. Brillouin, *Wave Propagation and Group Velocity* (1960).

# E006 · Energy Audit of an "Over-Unity" Device

**Purpose:** A protocol for testing any device claimed to output more energy than it takes in (toroidal coils, "scalar" generators, magnet motors). ([Concept 08](../docs/concepts/08-vortices-and-tori.md))
**Prior expectation:** ❌ Conservation of energy has never failed in a measured device. But the right response to a claim is to **measure it**, not dismiss it.

## Why most claims fail (the common mistakes)
| Mistake | What goes wrong |
|---|---|
| Multiplying peak voltage by peak current | For AC or pulsed signals, true power is the **average of instantaneous $v(t)\,i(t)$**. Peaks can overstate power by 10× or more. |
| Ignoring phase | In inductive circuits, current lags voltage. Apparent power (VA) is not real power (W). |
| Using a cheap multimeter on pulses | Many meters assume a sine wave and badly misread spikes. |
| Not closing the loop | Measuring "output" while an unmeasured battery or wall supply quietly feeds the system. |
| Too-short runs | Batteries and capacitors store energy. Any device can "output extra" for a while by draining them. |

## Protocol
1. **Measure input energy** with a data-logging power analyzer or a digital oscilloscope sampling voltage *and* current (via a shunt resistor or current probe) at at least 10× the highest signal frequency. Compute $E_{in} = \int v(t)i(t)\,dt$.
2. **Measure output energy** the same way, across a **resistive load** (a power resistor). Heat in a resistor is unambiguous.
3. **Account for storage.** Measure battery or capacitor state (voltage at rest) before and after. Run long enough that stored energy is under 1% of total energy moved.
4. **Best test: close the loop.** Feed the output back to the input and **disconnect the external source**. A genuine over-unity device keeps running indefinitely. Every claimed device to date has stopped.
5. **Calibrate.** Run the same measurement on a known device (an ordinary transformer) and confirm it gives efficiency < 100%.
6. **Publish everything:** raw waveforms, instrument models, probe calibration, and the analysis script.

## Result template
```
Device:            ___________
Run duration:      ______ s
E_in  (measured):  ______ J
E_out (measured):  ______ J
Δ stored energy:   ______ J
Efficiency = E_out / (E_in - ΔE_stored) = ______
Closed-loop self-run achieved?  yes / no   Duration: ______
```

## Safety
Pulsed coils can produce **lethal** voltage spikes. Use isolated probes and a fused supply, and never work alone on circuits above 50 V.

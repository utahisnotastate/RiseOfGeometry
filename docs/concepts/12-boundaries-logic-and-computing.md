# 12 · Drawing a Line: Boundaries, Logic, and the True Cost of Computing

> All of logic can be built from one act: drawing a boundary. And computing can, in principle, cost almost no energy. The only unavoidable cost is *forgetting*.

**Status:** ✅ Established (Laws of Form is a valid Boolean calculus; Landauer's principle, measured in 2012; reversible computing). ❌ Not supported: "zero-energy, zero-latency" computing that bypasses complexity limits.

---

## What everyone wishes they'd noticed sooner

**Two surprising facts that sound like mysticism but are solid:**

1. **Logic is geometry of the simplest kind.** In 1969 mathematician George Spencer-Brown showed you can rebuild all of Boolean logic (the logic inside every computer) from a single symbol: **a mark that draws a boundary**, dividing inside from outside. His book *Laws of Form* uses just two rules.

2. **Thinking isn't what costs energy. Forgetting is.** Rolf Landauer (IBM, 1961) proved that the only computation that *must* release heat is **erasing** information. Charles Bennett (1973) then showed that any computation can be done **reversibly**, without erasing, so in principle the energy cost can be made arbitrarily small. Today's chips use about a billion times more energy per operation than this limit. There's enormous room to improve.

## Explain it to a kid

Draw a circle on a blank page. Now there's an **inside** and an **outside**. That circle is a "yes/no." You've just made the simplest possible idea.

Spencer-Brown found two rules:
- Drawing the same circle twice side by side is the same as drawing it once. (Saying "yes, yes" means "yes.")
- A circle drawn *around* another circle cancels it, and you're back to a blank page. (Saying "not not" means nothing changed.)

With just those two rules, you can build all the logic a computer uses.

And the energy part: a calculator that could run backward and "un-think" every step would barely need to make heat. The heat comes from throwing away the scratch work.

## Examples you already know

- **"Not not true" = true.** That's Spencer-Brown's second rule in everyday English.
- **Venn diagrams** are logic drawn as boundaries.
- **Your laptop gets hot**, and much of that heat comes from constantly erasing and overwriting bits.
- **The undo button** is a crude kind of reversibility: your computer spends memory to avoid forgetting.

## The grown-up version

**Laws of Form, primary arithmetic.** Writing the mark as $\overline{\ \ }$ (a cross) and the empty space as the unmarked state:

$$
\text{Calling:}\quad \overline{\ \ }\ \overline{\ \ } = \overline{\ \ }
\qquad\qquad
\text{Crossing:}\quad \overline{\overline{\ \ }\,} = \ \ \ (\text{void})
$$

The resulting *primary algebra* is equivalent to Boolean algebra and to propositional logic (proved by Spencer-Brown and later formalized by others, e.g. Kauffman, Meguire). It's elegant and has influenced systems theory (von Foerster, Maturana, Varela, Luhmann). It is a notation, and it computes nothing a Boolean circuit can't.

**Landauer's principle.** Erasing one bit at temperature $T$ dissipates at least

$$
E_{\min} = k_B T \ln 2 \approx 2.9\times10^{-21}\ \text{J at room temperature}.
$$

Bérut et al. measured this limit directly with a colloidal particle in a laser trap (*Nature*, 2012). Bennett's reversible computing and modern **adiabatic** and **reversible logic** research aim to approach it. **Quantum computers** are necessarily reversible (unitary) during computation.

**Hard limits still apply.** The Margolus–Levitin theorem caps a system of energy $E$ at $2E/(\pi\hbar)$ operations per second, which is about **5.4 × 10⁵⁰ ops/s for 1 kg** (Seth Lloyd's "ultimate laptop," 2000). No computer, reversible or not, escapes this, and no known physics lets classical or quantum computers solve every exponential ($O(2^n)$) problem in polynomial time.

## Where the original notes went too far

- ✅ "Spencer-Brown's Laws of Form treats distinction as the primitive; Calling and Crossing are its axioms": **true.**
- ✅ "Conventional computers waste energy": **true**, by a factor of about a billion versus Landauer's limit.
- ❌ "A Fourth Law of Logic, $[A_1 \equiv \bar{A}_2]_3$, where opposites become identical at the boundary": **not part of Laws of Form or any accepted logic.** It comes from T. E. Bearden's writings. (Spencer-Brown does discuss self-reference and "imaginary" Boolean values, a genuinely interesting part of the book, but that's different.)
- ❌ "Boundary logic computes with zero energy and zero lag, bypassing $O(2^n)$": **not supported.** Reversible computing lowers heat but still takes time. Quantum computing speeds up specific problems (like factoring) but isn't known to solve NP-complete problems efficiently.

## Try it

- Pick up *Laws of Form* (it's short) or Louis Kauffman's free online introductions to boundary mathematics. Verify De Morgan's laws using only circles.
- **Reversible logic puzzle:** the Toffoli gate (inputs a, b, c → outputs a, b, c XOR (a AND b)) is reversible and universal. Show that running it twice returns the original inputs.

## Read more

- G. Spencer-Brown, *Laws of Form* (1969).
- L. H. Kauffman, "Laws of Form: An Exploration in Mathematics and Foundations" (lecture notes, University of Illinois at Chicago).
- R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM J. Res. Dev.* 5, 183 (1961).
- C. H. Bennett, "Logical Reversibility of Computation," *IBM J. Res. Dev.* 17, 525 (1973).
- A. Bérut et al., "Experimental verification of Landauer's principle," *Nature* 483, 187 (2012).
- S. Lloyd, "Ultimate physical limits to computation," *Nature* 406, 1047 (2000).

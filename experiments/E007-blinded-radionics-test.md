# E007 · Blinded Test of a Radionics / "Psychotronic" Device

**Purpose:** A fair protocol for testing any device whose result depends on an operator's sensation, such as the Hieronymus machine, "damplifier" ink diagrams, dowsing instruments, or pendulum readers. ([Claims ledger D07, D25](../docs/claims/ledger.md))
**Prior expectation:** ❌ No such device has passed a controlled, blinded test. Operators are usually sincere. Their sensations are real, but they're consistent with the **ideomotor effect** (tiny unconscious muscle movements guided by expectation).

## Design
1. **Agree on the claim in advance** with the operator. For example: *"The device can tell which of 10 identical sealed envelopes contains the sample."*
2. **Agree on a success criterion in advance.** With 10 envelopes and 20 trials, chance gives about 2 correct. Agree that, say, **8 or more correct out of 20** counts as success (chance probability about 0.04%).
3. **Double-blind:**
   - Person A prepares the envelopes and records which is which, then leaves.
   - Person B, who doesn't know the answer, randomizes the order and hands envelopes to the operator.
   - The operator and anyone in the room with them must not know the answer.
4. **Sham control:** in some trials, secretly disconnect or swap the device for an identical-looking dummy. If results are equally good with the dummy, the device isn't doing the work.
5. **Record everything**, including all trials. No dropping "bad days."
6. **Unblind only after all trials are recorded.**

## Scoring
```
Trials:         20
Correct:        ___
Chance expected: 2
p-value (binomial, p=0.1): ___
Sham trials correct: ___ / ___
```
Compute the p-value: `python -c "from math import comb; k=8; print(sum(comb(20,i)*0.1**i*0.9**(20-i) for i in range(k,21)))"`

## Why be this careful?
James Randi's foundation offered $1,000,000 for any paranormal claim passing a test like this from 1964 to 2015. Over 1,000 people applied. None passed a preliminary test. **A well-designed test is the fairest possible treatment of a claim.** If a device works, this is exactly how it would prove it.

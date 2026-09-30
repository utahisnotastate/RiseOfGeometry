# Contributing

Thanks for helping. This repository has one rule above all others: **every claim carries an honest label, and labels follow evidence.**

## Good contributions
- **Corrections.** A wrong number, a misattributed discovery, a broken reference.
- **Better explanations.** Clearer kid-level analogies or everyday examples.
- **New experiment data.** Add CSVs under `experiments/data/` (e.g. spiral counts from E002).
- **New tools.** Small, dependency-free Python scripts in `tools/` that reproduce a number or demonstrate an effect.
- **Label changes.** Moving a claim between ✅ / 🟡 / 🧪 / 📜 / ❌ in [docs/claims/ledger.md](docs/claims/ledger.md).

## Requirements for a label change
1. Cite **peer-reviewed** work or a reproducible experiment, with enough detail that someone else could repeat it.
2. Independent replication is required to move a claim to ✅.
3. Label changes go both ways. We'll happily downgrade something marked ✅ if new evidence warrants it.

## Style
- Each concept page follows the same layout: *one-line summary → status → what everyone wishes they'd noticed sooner → explain it to a kid → examples → grown-up version → where the original notes went too far → try it → read more.*
- Keep kid-level sections free of jargon.
- Math uses GitHub's `$...$` / `$$...$$` rendering.
- Tools use only the Python standard library and run with `python tools/<name>.py`.

## Not accepted
- Claims sourced to channeling, "future timelines," AI personas, or unnamed insiders. Evidence has to be checkable.
- Health or medical claims without clinical evidence.

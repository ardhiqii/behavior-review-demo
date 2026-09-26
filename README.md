# Behavior Review end-to-end demo

This disposable fixture validates the full old-commit/new-commit workflow.

- `ref/base` is the known-good baseline.
- `scenario-delta` changes rounding in `apply_discount`.
- `scenario-fixed` restores the original behavior.
- The same committed probe runs against every revision.

The fixture is for engineering validation only. Its generated reports must not
be presented as final production evidence.

## Run the scenario

From the repository root:

```powershell
behavior-review --repo . --base ref/base --head scenario-delta --run --json reports/scenario-delta.json --markdown reports/scenario-delta.md
behavior-review --repo . --base ref/base --head scenario-fixed --run --prior-report reports/scenario-delta.json --json reports/scenario-fixed.json --markdown reports/scenario-fixed.md
```

Expected outcomes:

- `scenario-delta`: `delta_observed`, old `179.99`, new `180.0`.
- `scenario-fixed`: `same_on_tested_cases`, linked to the earlier delta.

## Install the tool

This repository is a synthetic fixture for the public `behavior-review` tool. From the parent
directory, clone and install the engine beside this fixture first:

```powershell
cd ..
git clone https://github.com/webdev-testa/pocbobbin.git behavior-review-tool
python -m venv behavior-review-tool/.venv
behavior-review-tool/.venv/Scripts/pip install -e behavior-review-tool
cd behavior-review-demo
```

Then run the commands above from this repository. The `reports/` directory is intentionally
ignored; generated reports are local validation artifacts, not final production evidence.

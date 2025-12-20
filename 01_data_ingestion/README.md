Purpose
Small scripts and sample exporters that produce the raw telemetry CSV/JSON fixtures we use for demos and tests.

What belongs here
- Sample export scripts (e.g., export_sample.py when moved)
- Lightweight ingestion helpers that fetch/save local sample files
- CLI entrypoints for producing demo data

Acceptance criteria
- A script in this folder should be runnable locally to produce a small sample dataset (enough for demo and tests).
- Scripts must include a short usage note and a --sample or --dry-run mode.

TODO
- Move export_sample.py here in the next commit and add a one-line example command.

---

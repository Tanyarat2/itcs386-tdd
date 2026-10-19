# ITCS386: Python unit testing and TDD

Parts 0, A1-A8 (including optional A8), and B of W9-TDD_Lab_Exercise_v7.

## Run

Requires Python 3.10 or newer. From this directory:

```text
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest -q
```

On macOS/Linux use `.venv/bin/python` instead of `.venv\Scripts\python`.
With an active environment, `pytest -q` also works.

## Evidence and authorship

This lab was prepared with AI assistance at the student's request. Tests
were actually executed at each recorded stage; red commits intentionally
contain failing tests. The final revision is green. Files in `evidence/`
preserve the command, exit code, and output of each run. Git history
records the resulting red, green, and refactor stages with real commit
timestamps. The work was performed in an automated local workflow, not
an interactive VS Code session. No GitHub publication or course
submission has been performed.

`REFLECTION.md` is an evidence-based draft for the student to review;
it does not claim to know the student's feelings or prior experience.

# AGENTS.md — obsidian-construction-from-text

Guidance for agents working in this repository.

## What this repository is

A publication parser. It reads a book or paper — the texts in `texts/` — and turns it into an
Obsidian vault: one note per section or chapter, with links between them derived from the
document's own structure rather than from hand-made guesses. The output is meant to be browsed
and edited as notes, so the vault is the deliverable and the parser is the means.

Python 3.8 through 3.11. Distributed as `publication-parser`, with a console script of the same
name.

## Layout

| Path | Role |
|---|---|
| `src/` | The parser package |
| `process_publications.py` | Batch driver over a set of publications |
| `texts/` | Input texts |
| `obsidian/` | Generated vault output. **Generated** — see below |
| `examples/` | Worked examples |
| `docs/` | Documentation |
| `requirements.txt` | Runtime dependencies, including spaCy |
| `setup.py` | Declares `python_requires=">=3.8"` and the `publication-parser` console script |

## Commands

```bash
pip install -r requirements.txt
pip install -e .
publication-parser --help
python process_publications.py
```

spaCy's language model must be downloaded separately before parsing; a missing model is the
usual first failure.

## Working here

- **`obsidian/` is generated output, not source.** Edits there are overwritten on the next run
  and are not the fix for anything. Change the parser and regenerate.
- Note the tracked-file volume: the generated vault accounts for tens of thousands of files.
  Avoid repo-wide greps and diffs across `obsidian/` unless that is genuinely the question;
  scope to `src/`, `docs/` and `examples/`.
- **Python 3.8–3.11 only.** Do not introduce syntax, typing or standard-library usage that
  requires 3.12 or newer, and do not assume the newest spaCy — the pin in `requirements.txt`
  is what the parser is tested against.
- There is no test suite and no CI workflow. Verification is running the parser over a text in
  `texts/` and inspecting the produced notes; report the command and what you checked.
- Structure drives the note graph. A change to how sections are detected changes the shape of
  every generated vault, so treat that code as the sensitive part of the project.

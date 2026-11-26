# AGENTS.md — obsidian-construction-from-text

Guidance for agents working in this repository.

## What this repository is

The installed `publication-parser` command converts structured publication Markdown into publication notes, candidate entity pages, optional topic pages, and a JSON graph. Use the [documentation index](docs/README.md) for current setup and verification.

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
| `setup.py` | Declares `python_requires=">=3.11"` and the `publication-parser` console script |

## Commands

Run the [Python 3.11 setup and synthetic walkthrough](docs/usage.md). The compatibility wrapper attempts NLTK resource downloads. The installed entry point lets the documented fixture run offline after installation.

## Working here

- **`obsidian/` is generated output, not source.** Edits there are overwritten on the next run
  and are not the fix for anything. Change the parser and regenerate.
- Note the tracked-file volume: the generated vault accounts for tens of thousands of files.
  Avoid repo-wide greps and diffs across `obsidian/` unless that is genuinely the question;
  scope to `src/`, `docs/` and `examples/`.
- Use Python 3.11 with the pinned spaCy release and the compatible NumPy ABI.
- The existing unit checks are under `src/tests`. Use the documented fixture to check the shipped CLI and inspect the generated notes and graph.

- Structure drives the note graph. A change to how sections are detected changes the shape of
  every generated vault, so treat that code as the sensitive part of the project.

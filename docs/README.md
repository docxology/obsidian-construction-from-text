# obsidian-construction-from-text — Documentation

Publication Parser and Obsidian Knowledge Base Generator: processes structured
Markdown files from scientific publications, extracts entities and topics, and
creates an Obsidian knowledge base with parsed information linked to the
original text (from root `README.md`).

## Map

- `src/` — package code (version declared in `src/__init__.py`).
- `obsidian/` — generated/output Obsidian vault content.
- `examples/`, `texts/` — sample publications and text inputs.
- `process_publications.py` — entry-point script.
- `setup.py`, `requirements.txt` — packaging (pip; no console entry point is
  declared in `setup.py`).

## Run

```bash
pip install -r requirements.txt
python process_publications.py
```

(Invocation pattern taken from the root `README.md` and repo layout; check
`python process_publications.py --help` for current flags. No test suite or
build scripts are declared in the repo.)

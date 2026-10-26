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
- `setup.py`, `requirements.txt` — packaging (pip). `setup.py` declares the
  `publication-parser=src.cli:main` console script.

## Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
python process_publications.py
```

Use `python process_publications.py --help` for current flags
(`--texts_dir`, `--obsidian_dir`, `--skip_topics`, `--verbose`).

## Test

```bash
python -m unittest discover -s src/tests
```

No lint, typecheck, or build steps are configured in the repo.

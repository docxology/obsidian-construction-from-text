# Setup and offline walkthrough

Use Python 3.11 and install the repository from its root. The dependency list retains the spaCy 3.5.3 pin and limits NumPy to the compatible 1.x ABI.

```sh
uv venv --python 3.11
uv pip install -e .
. .venv/bin/activate
publication-parser --help
```

Use a fresh destination for the synthetic example. The installed entry point invokes the parser without the NLTK resource downloads performed by the compatibility wrapper at `process_publications.py`. The standard CLI uses capitalization and phrase rules for candidate extraction. `--skip_topics` also bypasses topic fitting for this one-file example.

```sh
vault_run="$(mktemp -d)"
publication-parser --texts_dir docs/examples/garden --obsidian_dir "$vault_run/vault" --skip_topics
python docs/examples/verify_vault.py "$vault_run/vault" --receipt output/fixture-summary.json
```

Read the publication note in `Publications/` or begin at `index.md` in Obsidian. The check reads the generated Markdown and `graph_data.json`. It requires a publication note, both fixture headings, vector `M1.1`, and a matching link from the publication to the Seed Library candidate.

| Option | Behavior |
|---|---|
| `--texts_dir` | Recursively reads files ending in `.md`; defaults to `texts` relative to the current directory. |
| `--obsidian_dir` | Destination for generated notes and graph data; defaults to `obsidian` relative to the current directory. |
| `--skip_topics` | Skips optional topic fitting and still produces entity notes. |
| `--verbose` | Enables debug logging. |

The command returns status 1 if it finds no parseable publications or cannot generate the vault. Existing output files with matching names can be overwritten, and stale files can remain in a reused destination.

Run the Markdown parser checks with `python -m unittest src.tests.test_markdown_parser -v`. Run the full unit suite with `python -m unittest discover -s src/tests`.

The audited baseline recorded three phrase-extraction failures in the entity extractor checks. The synthetic CLI walkthrough above checks a separate end-to-end behavior. [The backlog](backlog.md) records the outstanding parser and configuration work.

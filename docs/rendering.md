# Render and validate the methods manuscript

Run the [synthetic vault check](usage.md) from a clean project checkout. It writes `output/fixture-summary.json`, which supports the measured counts in the manuscript table. Use a separate [Template checkout](https://github.com/docxology/template/tree/87704feae0a4490ef7dad9c931d268e8c30273c2) at `87704feae0a4490ef7dad9c931d268e8c30273c2` with Pandoc, pandoc-crossref, and LaTeX available. See the [Template run guide](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/RUN_GUIDE.md) for those prerequisites.

Name the physical checkout directory `obsidian-construction-from-text` so the pinned validator can find the combined PDF.
Set `publication_checkout` to the absolute Publication Parser checkout path. From the Template checkout, use a fresh project slot.

```sh
uv sync --locked --no-dev
mkdir -p projects/working
ln -s "$publication_checkout" projects/working/obsidian-construction-from-text
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/obsidian-construction-from-text --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/obsidian-construction-from-text
```

The primary files are `output/pdf/obsidian-construction-from-text_combined.pdf`, `output/web/index.html`, and the validation and provenance reports in `output/reports/` within the project checkout. Check the fixture table, citation, and section ordering in both formats.

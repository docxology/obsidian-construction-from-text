# Markdown and vault format

The [garden fixture](examples/garden/garden_inventory_2026.md) demonstrates the text format. A first-line H1 provides a display title. The filename parser treats the final underscore-delimited segment as the year, the preceding segment as the title, and earlier segments as author text when the expected filename parts exist. Use the H1 for a multiword display title. The optional `__Paper Type:__` line supplies the paper type.

The parser recognizes ATX markers at levels 2–4. It records section titles and scans section bodies for markers such as `**Vector ID:** M1.1` and `**Vector Type:** Overview`. The publication note summarizes these sections and vectors. The parser uses pattern matching and its heading and metadata rules are narrower than a full Markdown parser.

The generator writes one `Publications/` note per parsed file. It writes distinct candidate `Entities/` notes and optional `Topics/` notes, an `index.md`, and `graph_data.json`. The graph records typed nodes and links such as `contains`. An edge describes a detected textual association, with no independent semantic validation. Candidate names and links can copy text from their input.

[Configuration defaults](../src/config.py) define recognized markers, folder names, exclusions, and topic extraction parameters. The standard CLI passes extraction settings without the optional NLP resource settings. Configuration for an explicit programmatic NLP path is separate from the default CLI.

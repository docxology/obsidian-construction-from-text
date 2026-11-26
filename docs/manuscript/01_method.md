# Method {#sec:method}

The parser recursively reads Markdown files and takes a display title from the first-line H1 when available. It identifies sections with configured heading markers and extracts vector identifiers and labels from the section text. The entity pass uses capitalization and phrase rules in the default command. Optional topic fitting can be bypassed independently.

The vault generator serializes publication, entity, and optional topic notes as Markdown. It uses NetworkX to represent typed nodes and relationships before writing `graph_data.json` [@hagberg2008networkx]. The JSON makes the constructed graph inspectable outside the Obsidian application. Generated links are candidate associations derived from the input text.

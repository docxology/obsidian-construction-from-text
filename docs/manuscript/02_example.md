# Synthetic garden inventory {#sec:example}

The checked-in fixture has a display title, two section headings, and an Overview vector labelled `M1.1`. The installed command runs against this one file and generates the vault in a fresh directory. The verification script reads the publication note, validates the expected seed-library candidate, and checks its `contains` edge in the graph.

| Observation | Fixture value |
|---|---:|
| Parsed publications | 1 |
| Recorded section headings | 2 |
| Recorded vector identifiers | 1 |
| Candidate entity notes | 13 |
| Graph nodes | 14 |
| Graph edges | 26 |

The `Topics/` directory has no notes because the fixture runs with topic fitting disabled. The publication note and index can be inspected as text.

"""Check artifacts produced by the documented synthetic CLI walkthrough."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    vault = args.vault
    publications = list((vault / "Publications").glob("*.md"))
    assert len(publications) == 1
    note = publications[0].read_text(encoding="utf-8")
    for fragment in ("# Garden Inventory", "overview", "inventory", "**M1.1**", "Seed Library"):
        assert fragment in note, fragment
    assert (vault / "index.md").is_file()
    entities = list((vault / "Entities").glob("*.md"))
    assert len(entities) == 13
    assert (vault / "Entities/seed-library.md").is_file()
    assert not list((vault / "Topics").glob("*.md"))

    graph = json.loads((vault / "graph_data.json").read_text(encoding="utf-8"))
    assert len(graph["nodes"]) == 14
    assert len(graph["edges"]) == 26
    assert any(
        edge["source"] == f"publication:{publications[0].stem}"
        and edge["target"] == "entity:seed-library"
        and edge["type"] == "contains"
        for edge in graph["edges"]
    )
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        summary = {
            "publications": len(publications),
            "candidate_entities": len(entities),
            "nodes": len(graph["nodes"]),
            "edges": len(graph["edges"]),
        }
        args.receipt.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("Verified one publication, two headings, one vector, and a graph of 14 nodes and 26 edges.")


if __name__ == "__main__":
    main()

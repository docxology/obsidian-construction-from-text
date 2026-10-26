# Publication Parser and Obsidian Knowledge Base Generator

This tool processes structured Markdown files from scientific publications, extracts entities and topics, and creates an Obsidian knowledge base with the parsed information linked to the original text.

## Overview

The system performs the following steps:

1. **Parse Markdown Files**: Reads structured Markdown files from the `texts/` directory, extracting sections, vectors, and metadata.
2. **Extract Entities**: Identifies entities (people, organizations, technologies, scientific concepts) mentioned in the publications.
3. **Extract Topics**: Uses NLP techniques to identify common topics across publications.
4. **Generate Obsidian Knowledge Base**: Creates a structured Obsidian vault in the `obsidian/` directory with:
   - Entity notes
   - Topic notes
   - Publication notes
   - Cross-linked references

## Installation

### Prerequisites

- Python 3.8–3.11 (the pinned NLP dependency versions ship wheels for these)
- pip (Python package manager)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/docxology/obsidian-construction-from-text.git
   cd obsidian-construction-from-text
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the required spaCy model:
   ```bash
   python -m spacy download en_core_web_md
   ```

## Usage

### Basic Usage

Run the main script to process all publications in the `texts/` directory and generate an Obsidian knowledge base in the `obsidian/` directory:

```bash
python process_publications.py
```

The same entry point is installed as the `publication-parser` console script when
the package itself is installed (`pip install .`).

### Command-line Options

```bash
python process_publications.py --texts_dir /path/to/texts --obsidian_dir /path/to/obsidian --skip_topics --verbose
```

Options:
- `--texts_dir`: Directory containing markdown files to parse (default: `texts/`)
- `--obsidian_dir`: Directory to output the Obsidian knowledge base (default: `obsidian/`)
- `--skip_topics`: Skip topic extraction for faster processing
- `--verbose`: Enable verbose logging

## Input Format

The system expects Markdown files in the `texts/` directory with a specific structure:

- Filenames should follow the pattern: `author_title_year.md` (the author
  segment may contain underscores, e.g. `de_nicola_graphene_2020.md`)
- The first line should be a level 1 heading with the paper title: `# Paper Title`
- Paper type should be specified as: `__Paper Type:__ Research`
- Sections should use level 2-4 headings (`##`, `###`, `####`)
- Vectors should be specified with:
  ```
  **Vector ID:** M1
  **Vector Type:** Overview
  ```

Example:
```markdown
# Test Paper Title

__Paper Type:__ Research

## M1: System Overview
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**
*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: This is a test description of a system.
```

## Output Structure

The system generates an Obsidian knowledge base in the `obsidian/` directory with the following structure:

```
obsidian/
├── index.md                  # Main index page
├── graph_data.json           # Graph visualization data
├── Entities/                 # Entity notes
│   ├── machine-learning.md
│   ├── artificial-intelligence.md
│   └── ...
├── Topics/                   # Topic notes
│   ├── topic-0.md
│   ├── topic-1.md
│   └── ...
└── Publications/             # Publication notes
    ├── author-paper-2023.md
    ├── another-paper-2022.md
    └── ...
```

## Development

### Running Tests

Run the test suite to verify the functionality:

```bash
python -m unittest discover -s src/tests
```

### Project Structure

```
.
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── process_publications.py   # Main script
├── texts/                    # Input Markdown files
├── obsidian/                 # Output Obsidian knowledge base
└── src/                      # Source code
    ├── __init__.py
    ├── config.py             # Configuration settings
    ├── main.py               # Main application logic
    ├── cli.py                # Command-line interface
    ├── parsers/              # Markdown parsing
    │   ├── __init__.py
    │   └── markdown_parser.py
    ├── extractors/           # Entity and topic extraction
    │   ├── __init__.py
    │   ├── entity_extractor.py
    │   └── topic_extractor.py
    ├── obsidian/             # Obsidian knowledge base generation
    │   ├── __init__.py
    │   └── obsidian_generator.py
    ├── utils/                # Utility functions
    │   ├── __init__.py
    │   ├── file_utils.py
    │   └── text_utils.py
    └── tests/                # Unit tests
        ├── __init__.py
        ├── test_markdown_parser.py
        └── test_entity_extractor.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This tool was designed to work with structured Markdown files containing scientific publication content.
- It uses spaCy for NLP processing and NetworkX for graph representation.
- The Obsidian knowledge base is designed to be opened with [Obsidian](https://obsidian.md/).
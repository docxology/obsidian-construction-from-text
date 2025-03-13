"""
Configuration settings for the Publication Parser and Obsidian Knowledge Base Generator.
"""

import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent.parent
TEXTS_DIR = os.path.join(BASE_DIR, "texts")
OBSIDIAN_DIR = os.path.join(BASE_DIR, "obsidian")

# Obsidian settings
OBSIDIAN_SETTINGS = {
    "entities_folder": "Entities",
    "topics_folder": "Topics",
    "publications_folder": "Publications",
    "index_filename": "index.md",
}

# Parser settings
PARSER_SETTINGS = {
    "vector_types": [
        "Overview", 
        "Description", 
        "Score", 
        "ParameterTable", 
        "Input", 
        "Output", 
        "Energy", 
        "Reaction",
        "Coupling", 
        "Information", 
        "Structure", 
        "Dynamic", 
        "Control", 
        "Scale", 
        "Constraint"
    ],
    "section_markers": ["##", "###", "####"],
    "vector_id_pattern": r"\*\*Vector ID:\*\* ([A-Z][0-9]+(?:\.[0-9]+)*)",
    "vector_type_pattern": r"\*\*Vector Type:\*\* ([A-Za-z]+)",
}

# Entity and topic extraction settings
EXTRACTION_SETTINGS = {
    "minimum_entity_length": 2,
    "excluded_entities": {
        "common_words": ["the", "and", "for", "with", "that", "this", "from", "their"],
        "stop_phrases": ["et al", "figure", "table", "section", "paper"],
    },
    "entity_types": [
        "PERSON", "ORG", "GPE", "WORK_OF_ART", "PRODUCT", "EVENT", 
        "SCIENTIFIC_CONCEPT", "TECHNOLOGY", "METHODOLOGY"
    ],
    "topic_extraction": {
        "min_df": 0.01,
        "max_df": 0.95,
        "n_components": 10,
        "n_top_words": 20,
    }
}

# NLP settings
NLP_SETTINGS = {
    "spacy_model": "en_core_web_md",
    "nltk_packages": ["punkt", "stopwords", "wordnet"],
} 
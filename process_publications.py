#!/usr/bin/env python
"""
Process publications and generate an Obsidian knowledge base.

This script is a convenience wrapper around the src/cli.py script.
"""

import os
import sys
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Ensure NLTK resources are downloaded
try:
    import nltk
    
    # Try to download required NLTK resources
    nltk_resources = ['punkt', 'stopwords', 'wordnet']
    for resource in nltk_resources:
        try:
            nltk.data.find(f'tokenizers/{resource}')
            logger.info(f"NLTK resource '{resource}' already downloaded")
        except LookupError:
            logger.info(f"Downloading NLTK resource: {resource}")
            nltk.download(resource, quiet=True)
    
    logger.info("NLTK resources initialized successfully")
except Exception as e:
    logger.warning(f"Failed to initialize NLTK components: {e}")
    logger.warning("Some features may not work correctly")

# Get the directory of this script
script_dir = Path(__file__).parent

# Execute the CLI script
sys.path.insert(0, str(script_dir))
from src.cli import main

if __name__ == "__main__":
    sys.exit(main()) 
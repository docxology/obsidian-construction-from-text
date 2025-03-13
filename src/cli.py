#!/usr/bin/env python
"""
Command-line interface for the publication parser and Obsidian knowledge base generator.
"""

import os
import sys
import logging
from pathlib import Path

# Add the parent directory to sys.path to allow importing the src package
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.main import main

if __name__ == "__main__":
    # Configure logging for CLI usage
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Run the main function
    sys.exit(main()) 
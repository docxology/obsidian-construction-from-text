#!/usr/bin/env python
"""
Example of how to use the publication parser programmatically.

This script demonstrates how to use the publication parser and Obsidian knowledge base
generator as a library in your own Python code.
"""

import os
import sys
import logging
from pathlib import Path

# Add the parent directory to sys.path to allow importing the src package
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import PARSER_SETTINGS, EXTRACTION_SETTINGS, OBSIDIAN_SETTINGS
from src.parsers import MarkdownParser
from src.extractors import EntityExtractor, TopicExtractor
from src.obsidian import ObsidianGenerator
from src.utils.file_utils import ensure_directory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def process_publications(texts_dir, obsidian_dir, skip_topics=False):
    """
    Process publications and generate an Obsidian knowledge base.
    
    Args:
        texts_dir: Directory containing markdown files to parse
        obsidian_dir: Directory to output the Obsidian knowledge base
        skip_topics: Whether to skip topic extraction
        
    Returns:
        True if the knowledge base was generated successfully, False otherwise
    """
    # Ensure the output directory exists
    ensure_directory(obsidian_dir)
    
    logger.info(f"Processing publications from {texts_dir}")
    logger.info(f"Generating Obsidian knowledge base in {obsidian_dir}")
    
    # Step 1: Parse markdown files
    logger.info("Step 1: Parsing markdown files")
    markdown_parser = MarkdownParser(PARSER_SETTINGS)
    parsed_publications = markdown_parser.parse_directory(texts_dir)
    
    logger.info(f"Parsed {len(parsed_publications)} publications")
    
    # Step 2: Extract entities
    logger.info("Step 2: Extracting entities")
    entity_extractor = EntityExtractor(EXTRACTION_SETTINGS)
    entity_extraction_results = entity_extractor.extract_entities_from_publications(parsed_publications)
    
    # Step 3: Extract topics (optional)
    topic_extraction_results = {}
    if not skip_topics:
        logger.info("Step 3: Extracting topics")
        topic_extractor = TopicExtractor(EXTRACTION_SETTINGS)
        topic_extraction_results = topic_extractor.extract_topics(parsed_publications)
    else:
        logger.info("Skipping topic extraction")
        topic_extraction_results = {'topics': [], 'document_topics': []}
    
    # Step 4: Generate Obsidian knowledge base
    logger.info("Step 4: Generating Obsidian knowledge base")
    obsidian_config = {**OBSIDIAN_SETTINGS, 'obsidian_dir': obsidian_dir}
    obsidian_generator = ObsidianGenerator(obsidian_config)
    
    # Combine results for the generator
    combined_results = {
        'parsed_publications': parsed_publications,
        'entity_extraction': entity_extraction_results,
        'topic_extraction': topic_extraction_results
    }
    
    success = obsidian_generator.generate_knowledge_base(combined_results)
    
    if success:
        logger.info("Successfully generated Obsidian knowledge base")
        logger.info(f"Output directory: {obsidian_dir}")
    else:
        logger.error("Failed to generate Obsidian knowledge base")
    
    return success

if __name__ == "__main__":
    # Example usage
    texts_dir = os.path.join(Path(__file__).parent.parent, "texts")
    obsidian_dir = os.path.join(Path(__file__).parent.parent, "obsidian")
    
    # Process a subset of publications (first 5 files)
    subset_dir = os.path.join(Path(__file__).parent, "subset")
    ensure_directory(subset_dir)
    
    # Create a subset of publications for demonstration
    import shutil
    from glob import glob
    
    # Get the first 5 markdown files
    markdown_files = glob(os.path.join(texts_dir, "*.md"))[:5]
    
    # Copy them to the subset directory
    for file in markdown_files:
        shutil.copy(file, subset_dir)
    
    logger.info(f"Created subset of {len(markdown_files)} publications in {subset_dir}")
    
    # Process the subset
    process_publications(subset_dir, obsidian_dir, skip_topics=True)
    
    logger.info("Example completed. Open the Obsidian knowledge base in Obsidian to explore the results.") 
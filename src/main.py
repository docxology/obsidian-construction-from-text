"""
Main application for parsing publications, extracting entities and topics,
and generating an Obsidian knowledge base.
"""

import os
import sys
import logging
import argparse
from typing import Dict, List, Any
import traceback

from .config import PARSER_SETTINGS, EXTRACTION_SETTINGS, OBSIDIAN_SETTINGS, TEXTS_DIR, OBSIDIAN_DIR, NLP_SETTINGS
from .parsers import MarkdownParser
from .extractors import EntityExtractor, TopicExtractor
from .obsidian import ObsidianGenerator
from .utils.file_utils import ensure_directory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def process_publications(texts_dir: str, obsidian_dir: str, skip_topics: bool = False, verbose: bool = False) -> bool:
    """
    Process publications and generate an Obsidian knowledge base.
    
    Args:
        texts_dir: Directory containing markdown files to parse
        obsidian_dir: Directory to output the Obsidian knowledge base
        skip_topics: Whether to skip topic extraction
        verbose: Whether to enable verbose logging
        
    Returns:
        True if the knowledge base was generated successfully, False otherwise
    """
    # Set logging level based on verbose flag
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Ensure the output directory exists
        ensure_directory(obsidian_dir)
        
        logger.info(f"Processing publications from {texts_dir}")
        logger.info(f"Generating Obsidian knowledge base in {obsidian_dir}")
        
        # Step 1: Parse markdown files
        logger.info("Step 1: Parsing markdown files")
        markdown_parser = MarkdownParser(PARSER_SETTINGS)
        parsed_publications = markdown_parser.parse_directory(texts_dir)
        
        if not parsed_publications:
            logger.error(f"No publications found in {texts_dir}")
            return False
            
        logger.info(f"Parsed {len(parsed_publications)} publications")
        
        # Step 2: Extract entities
        logger.info("Step 2: Extracting entities")
        entity_extractor = EntityExtractor(EXTRACTION_SETTINGS)
        entity_extraction_results = entity_extractor.extract_entities_from_publications(parsed_publications)
        
        if not entity_extraction_results.get('all_entities'):
            logger.warning("No entities were extracted from publications")
        
        # Step 3: Extract topics (optional)
        topic_extraction_results = {'topics': [], 'document_topics': []}
        if not skip_topics:
            try:
                logger.info("Step 3: Extracting topics")
                topic_extractor = TopicExtractor(EXTRACTION_SETTINGS)
                topic_extraction_results = topic_extractor.extract_topics(parsed_publications)
                
                if not topic_extraction_results.get('topics'):
                    logger.warning("No topics were extracted from publications")
            except Exception as e:
                logger.error(f"Topic extraction failed: {e}")
                logger.error(traceback.format_exc())
                logger.warning("Continuing without topics...")
        else:
            logger.info("Skipping topic extraction")
        
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
            return True
        else:
            logger.error("Failed to generate Obsidian knowledge base")
            return False
    except Exception as e:
        logger.error(f"Error processing publications: {e}")
        logger.error(traceback.format_exc())
        return False

def main() -> int:
    """
    Main entry point for the application when run as a script.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = argparse.ArgumentParser(description="Process publications and generate an Obsidian knowledge base")
    parser.add_argument("--texts_dir", default="texts", help="Directory containing markdown files to parse")
    parser.add_argument("--obsidian_dir", default="obsidian", help="Directory to output the Obsidian knowledge base")
    parser.add_argument("--skip_topics", action="store_true", help="Skip topic extraction for faster processing")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    success = process_publications(
        texts_dir=args.texts_dir,
        obsidian_dir=args.obsidian_dir,
        skip_topics=args.skip_topics,
        verbose=args.verbose
    )
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main()) 
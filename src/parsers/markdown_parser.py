"""Markdown parser for extracting structured content from publications."""

import os
import re
import logging
from typing import Dict, List, Any

from ..utils.file_utils import read_markdown_file, get_file_metadata
from ..utils.text_utils import (
    extract_section_content,
    extract_vector_info
)

logger = logging.getLogger(__name__)

class MarkdownParser:
    """
    Parser for structured markdown files containing publication information.
    
    This parser is designed to extract sections, vectors, and content from
    structured markdown files following a specific format.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the MarkdownParser.
        
        Args:
            config: Configuration dictionary containing parser settings
        """
        self.config = config
        self.vector_types = config.get('vector_types', [])
        self.section_markers = config.get('section_markers', ['##', '###', '####'])
        self.vector_id_pattern = config.get('vector_id_pattern', r'\*\*Vector ID:\*\* ([A-Z][0-9]+(?:\.[0-9]+)*)')
        self.vector_type_pattern = config.get('vector_type_pattern', r'\*\*Vector Type:\*\* ([A-Za-z]+)')
    
    def parse_file(self, filepath: str) -> Dict[str, Any]:
        """
        Parse a markdown file and extract structured content.
        
        Args:
            filepath: Path to the markdown file to parse
            
        Returns:
            Dictionary containing the parsed content
        """
        logger.info(f"Parsing file: {filepath}")
        
        content = read_markdown_file(filepath)
        if not content:
            logger.error(f"Failed to read file: {filepath}")
            return {}
        
        # Get file metadata from filename
        metadata = get_file_metadata(filepath)
        
        # Extract the title from the first line if it starts with a # heading
        title_match = re.match(r'# (.*?)(:?\n|$)', content)
        if title_match:
            metadata['title_text'] = title_match.group(1).strip()
        
        # Extract paper type if available
        paper_type_match = re.search(r'__Paper Type:__ (.*?)(\n|$)', content)
        if paper_type_match:
            metadata['paper_type'] = paper_type_match.group(1).strip()
        
        # Extract sections from the content
        sections = extract_section_content(content, self.section_markers)
        
        # Parse vectors from sections
        vectors = []
        for section in sections:
            vector_info = extract_vector_info(
                section['content'],
                self.vector_id_pattern,
                self.vector_type_pattern
            )
            
            if vector_info:
                # Add section context to the vector
                vector_info['section_title'] = section['title']
                vector_info['section_level'] = section['level']
                vector_info['section_content'] = section['content']
                vectors.append(vector_info)
        
        result = {
            'metadata': metadata,
            'sections': sections,
            'vectors': vectors
        }
        
        logger.info(f"Parsed {len(sections)} sections and {len(vectors)} vectors from {filepath}")
        return result
    
    def parse_directory(self, directory: str) -> List[Dict[str, Any]]:
        """
        Parse all markdown files in a directory.
        
        Args:
            directory: Directory containing markdown files to parse
            
        Returns:
            List of dictionaries with parsed content
        """
        logger.info(f"Parsing directory: {directory}")
        
        results = []
        filenames = []
        
        # Get all markdown files in the directory
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    filenames.append(os.path.join(root, file))
        
        # Parse each file
        for filename in filenames:
            parsed = self.parse_file(filename)
            if parsed:
                results.append(parsed)
        
        logger.info(f"Parsed {len(results)} files from {directory}")
        return results 
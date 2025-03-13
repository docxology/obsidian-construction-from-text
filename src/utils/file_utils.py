"""Utility functions for file operations."""

import os
import glob
from pathlib import Path
from typing import List, Dict, Any, Optional
import yaml
import logging

logger = logging.getLogger(__name__)

def get_markdown_files(directory: str) -> List[str]:
    """
    Get a list of all markdown files in the given directory.
    
    Args:
        directory: The directory to search for markdown files
        
    Returns:
        A list of paths to markdown files
    """
    if not os.path.exists(directory):
        logger.error(f"Directory {directory} does not exist")
        return []
    
    pattern = os.path.join(directory, "*.md")
    return glob.glob(pattern)

def ensure_directory(directory: str) -> bool:
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        directory: The directory to ensure exists
        
    Returns:
        True if the directory exists or was created, False otherwise
    """
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Failed to create directory {directory}: {e}")
        return False

def load_yaml_front_matter(markdown_content: str) -> Dict[str, Any]:
    """
    Extract YAML front matter from the markdown content if it exists.
    
    Args:
        markdown_content: The content of the markdown file
        
    Returns:
        A dictionary with the parsed YAML front matter, or an empty dict if none exists
    """
    if not markdown_content.startswith('---'):
        return {}
    
    try:
        # Find the end of the YAML front matter
        end_index = markdown_content.find('---', 3)
        if end_index == -1:
            return {}
        
        # Extract and parse the YAML front matter
        front_matter = markdown_content[3:end_index].strip()
        return yaml.safe_load(front_matter) or {}
    except Exception as e:
        logger.error(f"Failed to parse YAML front matter: {e}")
        return {}

def get_file_metadata(filepath: str) -> Dict[str, Any]:
    """
    Extract metadata from a markdown file filename.
    
    Expects filenames in the format: author_title_year.md
    
    Args:
        filepath: Path to the markdown file
        
    Returns:
        A dictionary with the extracted metadata
    """
    filename = os.path.basename(filepath)
    basename, _ = os.path.splitext(filename)
    
    parts = basename.split('_')
    metadata = {
        "filepath": filepath,
        "filename": filename,
        "basename": basename,
    }
    
    # Try to extract author, title, year if the format matches
    if len(parts) >= 3:
        metadata["author"] = parts[0]
        metadata["year"] = parts[-1]
        metadata["title"] = '_'.join(parts[1:-1])
    
    return metadata

def save_markdown_file(content: str, filepath: str) -> bool:
    """
    Save content to a markdown file.
    
    Args:
        content: The content to save
        filepath: The path to save the content to
        
    Returns:
        True if the file was saved successfully, False otherwise
    """
    try:
        directory = os.path.dirname(filepath)
        ensure_directory(directory)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        logger.error(f"Failed to save file {filepath}: {e}")
        return False

def read_markdown_file(filepath: str) -> Optional[str]:
    """
    Read the content of a markdown file.
    
    Args:
        filepath: The path to the file to read
        
    Returns:
        The content of the file, or None if the file could not be read
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Failed to read file {filepath}: {e}")
        return None 
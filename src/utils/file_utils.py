"""Utility functions for file operations."""

import os
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

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

def get_file_metadata(filepath: str) -> Dict[str, Any]:
    """
    Extract metadata from a markdown file filename.
    
    Expects filenames in the format: author_title_year.md, where the author
    segment may itself contain underscores (for example
    `de_nicola_graphene_2020.md`).
    
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
        metadata["author"] = '_'.join(parts[:-2])
        metadata["year"] = parts[-1]
        metadata["title"] = parts[-2]
    
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
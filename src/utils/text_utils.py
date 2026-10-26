"""Utility functions for text processing."""

import re
import string
from typing import List, Dict, Any, Set, Tuple
import logging

logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and normalizing.
    
    Args:
        text: The text to clean
        
    Returns:
        Cleaned text
    """
    # Replace multiple whitespace with a single space
    text = re.sub(r'\s+', ' ', text)
    # Strip leading and trailing whitespace
    return text.strip()

def extract_section_content(text: str, section_markers: List[str]) -> List[Dict[str, Any]]:
    """
    Extract sections from markdown text based on heading markers.
    
    Args:
        text: The markdown text to process
        section_markers: List of section heading markers (e.g., ["##", "###"])
        
    Returns:
        List of dictionaries with section information
    """
    sections = []
    
    # Create a pattern to match any of the section markers
    marker_pattern = '|'.join([re.escape(marker) for marker in section_markers])
    pattern = f"({marker_pattern}) ([^\n]+)"
    
    # Find all section headings
    matches = re.finditer(pattern, text)
    
    # Track the start positions of each section
    positions = []
    for match in matches:
        level = len(match.group(1).strip())
        # Headings may be wrapped in markdown emphasis markers (### **1.1 Title**)
        title = match.group(2).strip().strip('*').strip()
        positions.append({
            'start': match.start(),
            'level': level,
            'title': title
        })
    
    # Process each section to extract its content
    for i, pos in enumerate(positions):
        # The content extends to the next section or the end of the text
        end = positions[i+1]['start'] if i < len(positions) - 1 else len(text)
        
        section_text = text[pos['start']:end]
        # Remove the heading from the section text
        section_text = re.sub(f"{re.escape(section_markers[pos['level']-2])} {re.escape(pos['title'])}\n", '', section_text, count=1)
        
        sections.append({
            'level': pos['level'],
            'title': pos['title'],
            'content': section_text.strip()
        })
    
    return sections

def extract_vector_info(section_content: str, vector_id_pattern: str, vector_type_pattern: str) -> Dict[str, Any]:
    """
    Extract vector information from section content.
    
    Args:
        section_content: The content of a section
        vector_id_pattern: Regex pattern to extract vector ID
        vector_type_pattern: Regex pattern to extract vector type
        
    Returns:
        Dictionary with vector information
    """
    vector_info = {}
    
    # Extract Vector ID
    vector_id_match = re.search(vector_id_pattern, section_content)
    if vector_id_match:
        vector_info['vector_id'] = vector_id_match.group(1)
    
    # Extract Vector Type
    vector_type_match = re.search(vector_type_pattern, section_content)
    if vector_type_match:
        vector_info['vector_type'] = vector_type_match.group(1)
    
    # Extract content based on the vector type structure
    # This is a simplified approach and may need to be customized
    content_start = section_content.find('Content:')
    if content_start != -1:
        content = section_content[content_start + len('Content:'):].strip()
        end_markers = ['CT-GIN Mapping:', 'Implicit/Explicit:', 'Score:', 'Table:']
        
        for marker in end_markers:
            marker_pos = content.find(marker)
            if marker_pos != -1:
                content = content[:marker_pos].strip()
                break
        
        vector_info['content'] = content
    
    return vector_info

def extract_entities_from_text(text: str, excluded_entities: Dict[str, List[str]], min_length: int = 2) -> Set[str]:
    """
    Extract potential entities from text using simple heuristics.
    
    This is a basic implementation. For production, consider using a more sophisticated NLP approach.
    
    Args:
        text: The text to extract entities from
        excluded_entities: Dictionary of excluded entity lists
        min_length: Minimum length of an entity word
        
    Returns:
        Set of extracted entities
    """
    # Simple entity extraction based on capitalized words
    words = re.findall(r'\b[A-Z][a-zA-Z]+\b', text)
    
    # Filter out common words and short words
    excluded_words = set(word.lower() for word in excluded_entities.get('common_words', []))
    excluded_phrases = set(phrase.lower() for phrase in excluded_entities.get('stop_phrases', []))
    
    entities = set()
    
    for word in words:
        if (len(word) >= min_length and 
            word.lower() not in excluded_words and
            word.lower() not in excluded_phrases):
            entities.add(word)
    
    # Extract multi-word entities (noun phrases)
    # This is a simple approach using capitalized phrases
    phrases = re.findall(r'\b[A-Z][a-zA-Z]+(?: [A-Za-z]+){1,5}\b', text)
    
    for phrase in phrases:
        is_valid = True
        for excluded in excluded_phrases:
            if excluded in phrase.lower():
                is_valid = False
                break
        
        if is_valid and len(phrase) >= min_length:
            entities.add(phrase)
    
    return entities

def normalize_entity_name(entity: str) -> str:
    """
    Normalize entity names for consistent references.
    
    Args:
        entity: The entity name to normalize
        
    Returns:
        Normalized entity name
    """
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    normalized = entity.translate(translator)
    
    # Convert to title case for consistency
    normalized = normalized.title()
    
    # Remove extra whitespace
    normalized = ' '.join(normalized.split())
    
    return normalized

def create_obsidian_link(text: str, link: str) -> str:
    """
    Create an Obsidian-style link.
    
    Args:
        text: The visible text
        link: The target link
        
    Returns:
        Obsidian-style link
    """
    return f"[[{link}|{text}]]"

def generate_slug(text: str) -> str:
    """
    Generate a slug from text for file naming.
    
    Args:
        text: The text to convert to a slug
        
    Returns:
        Slug string
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    slug = text.translate(translator).lower()
    
    # Replace spaces with hyphens
    slug = '-'.join(slug.split())
    
    return slug 
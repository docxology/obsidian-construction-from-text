"""Entity extraction from publication content."""

import logging
import re
from typing import Dict, List, Any, Set, Optional
from collections import defaultdict

import spacy
import nltk
from nltk.corpus import stopwords

from ..utils.text_utils import (
    extract_entities_from_text,
    normalize_entity_name,
    clean_text
)

logger = logging.getLogger(__name__)

class EntityExtractor:
    """
    Extract entities from publication content.
    
    Uses a combination of rule-based and NLP approaches to identify entities
    such as people, organizations, technologies, and scientific concepts.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the EntityExtractor.
        
        Args:
            config: Configuration dictionary containing extraction settings
        """
        self.config = config
        self.minimum_entity_length = config.get('minimum_entity_length', 2)
        self.excluded_entities = config.get('excluded_entities', {
            'common_words': [],
            'stop_phrases': []
        })
        self.entity_types = config.get('entity_types', [])
        
        # Initialize NLP components if available
        self.nlp = None
        self.nltk_initialized = False
        
        try:
            # Try to load the spaCy model
            if 'spacy_model' in config:
                logger.info(f"Loading spaCy model: {config['spacy_model']}")
                self.nlp = spacy.load(config['spacy_model'])
            
            # Initialize NLTK components
            if 'nltk_packages' in config:
                for package in config['nltk_packages']:
                    logger.info(f"Downloading NLTK package: {package}")
                    nltk.download(package, quiet=True)
                self.nltk_initialized = True
                
        except Exception as e:
            logger.warning(f"Failed to initialize NLP components: {e}")
            logger.warning("Falling back to rule-based entity extraction")
    
    def extract_entities(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract entities from parsed publication content.
        
        Args:
            content: Parsed publication content
            
        Returns:
            Dictionary with extracted entities and their occurrences
        """
        entities = defaultdict(lambda: defaultdict(list))
        
        # Extract entities from sections
        for section in content.get('sections', []):
            section_title = section.get('title', '')
            section_content = section.get('content', '')
            
            # Extract entities from section content
            section_entities = self._extract_entities_from_text(section_content)
            
            # Add entities with their source section
            for entity in section_entities:
                entity_normalized = normalize_entity_name(entity)
                entities[entity_normalized]['sections'].append({
                    'title': section_title,
                    'content': section_content
                })
        
        # Extract entities from vectors
        for vector in content.get('vectors', []):
            vector_id = vector.get('vector_id', '')
            vector_type = vector.get('vector_type', '')
            vector_content = vector.get('content', '')
            
            # Extract entities from vector content
            vector_entities = self._extract_entities_from_text(vector_content)
            
            # Add entities with their source vector
            for entity in vector_entities:
                entity_normalized = normalize_entity_name(entity)
                entities[entity_normalized]['vectors'].append({
                    'id': vector_id,
                    'type': vector_type,
                    'content': vector_content
                })
        
        # Convert defaultdict to regular dict for serialization
        return {
            'metadata': content.get('metadata', {}),
            'entities': {
                entity: dict(occurrences) for entity, occurrences in entities.items()
            }
        }
    
    def _extract_entities_from_text(self, text: str) -> Set[str]:
        """
        Extract entities from text using NLP and rule-based approaches.
        
        Args:
            text: Text to extract entities from
            
        Returns:
            Set of extracted entities
        """
        entities = set()
        text = clean_text(text)
        
        # Use spaCy NER if available
        if self.nlp:
            doc = self.nlp(text)
            for ent in doc.ents:
                if ent.label_ in self.entity_types:
                    entities.add(ent.text)
        
        # Use rule-based extraction as fallback or complement
        rule_based_entities = extract_entities_from_text(
            text,
            self.excluded_entities,
            self.minimum_entity_length
        )
        entities.update(rule_based_entities)
        
        return entities
    
    def extract_entities_from_publications(self, publications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extract entities from multiple publications.
        
        Args:
            publications: List of parsed publications
            
        Returns:
            Dictionary with extracted entities across all publications
        """
        all_entities = {}
        publication_entities = []
        
        # Process each publication
        for publication in publications:
            pub_entities = self.extract_entities(publication)
            publication_entities.append(pub_entities)
            
            # Aggregate entities across publications
            for entity, occurrences in pub_entities.get('entities', {}).items():
                if entity not in all_entities:
                    all_entities[entity] = {
                        'publications': [],
                        'total_occurrences': 0
                    }
                
                # Add this publication to the entity's occurrences
                all_entities[entity]['publications'].append({
                    'metadata': publication.get('metadata', {}),
                    'occurrences': occurrences
                })
                
                # Count total occurrences across sections and vectors
                section_count = len(occurrences.get('sections', []))
                vector_count = len(occurrences.get('vectors', []))
                all_entities[entity]['total_occurrences'] += section_count + vector_count
        
        return {
            'all_entities': all_entities,
            'publication_entities': publication_entities
        } 
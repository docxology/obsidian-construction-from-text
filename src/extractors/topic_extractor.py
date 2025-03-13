"""Topic extraction from publication content."""

import logging
import re
from typing import Dict, List, Any, Set, Optional, Tuple
from collections import defaultdict

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

from ..utils.text_utils import clean_text

logger = logging.getLogger(__name__)

class TopicExtractor:
    """
    Extract topics from publication content.
    
    Uses NLP techniques to identify topics across publications
    and within individual documents.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the TopicExtractor.
        
        Args:
            config: Configuration dictionary containing extraction settings
        """
        self.config = config
        self.topic_config = config.get('topic_extraction', {})
        self.min_df = self.topic_config.get('min_df', 0.01)
        self.max_df = self.topic_config.get('max_df', 0.95)
        self.n_components = self.topic_config.get('n_components', 10)
        self.n_top_words = self.topic_config.get('n_top_words', 20)
        
        # Initialize NLP components
        self.nltk_initialized = False
        self.stop_words = None
        self.lemmatizer = None
        
        self._ensure_nltk_resources()
    
    def _ensure_nltk_resources(self):
        """Ensure that NLTK resources are properly downloaded."""
        try:
            # Try to download required NLTK resources
            nltk_resources = ['punkt', 'stopwords', 'wordnet']
            for resource in nltk_resources:
                try:
                    nltk.data.find(f'tokenizers/{resource}')
                except LookupError:
                    logger.info(f"Downloading NLTK resource: {resource}")
                    nltk.download(resource, quiet=True)
            
            # Initialize NLTK components
            self.stop_words = set(stopwords.words('english'))
            self.lemmatizer = WordNetLemmatizer()
            self.nltk_initialized = True
            logger.info("NLTK resources initialized successfully")
        except Exception as e:
            logger.warning(f"Failed to initialize NLTK components: {e}")
            logger.warning("Using basic stop words and no lemmatization")
            self.stop_words = set(['the', 'and', 'to', 'of', 'a', 'in', 'that', 'is'])
    
    def extract_topics(self, publications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extract topics from multiple publications.
        
        Args:
            publications: List of parsed publications
            
        Returns:
            Dictionary with extracted topics
        """
        # Prepare documents for topic modeling
        docs = []
        doc_metadata = []
        
        for publication in publications:
            # Extract all text content from the publication
            content = self._extract_publication_text(publication)
            if content:
                docs.append(content)
                doc_metadata.append(publication.get('metadata', {}))
        
        if not docs:
            logger.warning("No documents to extract topics from")
            return {'topics': [], 'document_topics': []}
        
        try:
            # Create document-term matrix
            logger.info("Creating document-term matrix")
            tfidf_vectorizer = TfidfVectorizer(
                max_df=self.max_df,
                min_df=self.min_df,
                stop_words='english',
                tokenizer=self._tokenize_and_preprocess if self.nltk_initialized else None
            )
            
            tfidf = tfidf_vectorizer.fit_transform(docs)
            
            # Extract topics using NMF
            logger.info(f"Extracting {self.n_components} topics")
            nmf = NMF(n_components=self.n_components, random_state=1).fit(tfidf)
            
            # Get feature names for the vectorizer
            feature_names = tfidf_vectorizer.get_feature_names_out()
            
            # Extract topics
            topics = []
            for topic_idx, topic in enumerate(nmf.components_):
                top_indices = topic.argsort()[:-self.n_top_words - 1:-1]
                top_terms = [feature_names[i] for i in top_indices]
                
                topics.append({
                    'id': topic_idx,
                    'name': f"Topic {topic_idx}",
                    'description': self._generate_topic_description(top_terms),
                    'top_terms': top_terms,
                    'weight': float(topic.sum())
                })
            
            # Extract document-topic assignments
            document_topics = []
            topic_document_matrix = nmf.transform(tfidf)
            
            for doc_idx, doc_topics in enumerate(topic_document_matrix):
                # Get the top topics for this document
                top_topic_indices = doc_topics.argsort()[:-4:-1]
                
                doc_topics_info = []
                for topic_idx in top_topic_indices:
                    if doc_topics[topic_idx] > 0.1:  # Only include topics with significant weight
                        doc_topics_info.append({
                            'topic_id': int(topic_idx),
                            'topic_name': f"Topic {topic_idx}",
                            'weight': float(doc_topics[topic_idx])
                        })
                
                # Add the document's topic assignments
                document_topics.append({
                    'metadata': doc_metadata[doc_idx],
                    'topics': doc_topics_info
                })
            
            return {
                'topics': topics,
                'document_topics': document_topics
            }
        
        except Exception as e:
            logger.error(f"Failed to extract topics: {e}")
            # Return empty results if topic extraction fails
            return {'topics': [], 'document_topics': []}
    
    def _extract_publication_text(self, publication: Dict[str, Any]) -> str:
        """
        Extract all text content from a publication.
        
        Args:
            publication: Parsed publication content
            
        Returns:
            Concatenated text content
        """
        texts = []
        
        # Add texts from sections
        for section in publication.get('sections', []):
            texts.append(section.get('content', ''))
        
        # Add texts from vectors
        for vector in publication.get('vectors', []):
            if 'content' in vector:
                texts.append(vector.get('content', ''))
        
        # Clean and join all texts
        return ' '.join(clean_text(text) for text in texts if text)
    
    def _tokenize_and_preprocess(self, text: str) -> List[str]:
        """
        Tokenize and preprocess text for topic modeling.
        
        Args:
            text: Text to preprocess
            
        Returns:
            List of preprocessed tokens
        """
        try:
            # Tokenize
            tokens = word_tokenize(text.lower())
            
            # Remove punctuation and short words
            tokens = [token for token in tokens if token.isalpha() and len(token) > 2]
            
            # Remove stop words
            if self.stop_words:
                tokens = [token for token in tokens if token not in self.stop_words]
            
            # Lemmatize if available
            if self.lemmatizer:
                tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
            
            return tokens
        except Exception as e:
            logger.warning(f"Error in tokenization: {e}")
            # Fallback to simple whitespace tokenization
            return [token.lower() for token in text.split() if len(token) > 2]
    
    def _generate_topic_description(self, top_terms: List[str]) -> str:
        """
        Generate a human-readable description of a topic.
        
        Args:
            top_terms: List of top terms for the topic
            
        Returns:
            Topic description
        """
        # Use the top 5 terms to generate a description
        return f"Topics related to {', '.join(top_terms[:5])}" 
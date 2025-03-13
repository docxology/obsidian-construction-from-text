"""Tests for the entity extractor."""

import unittest
from unittest.mock import patch

from src.extractors.entity_extractor import EntityExtractor
from src.config import EXTRACTION_SETTINGS

class TestEntityExtractor(unittest.TestCase):
    """Test cases for the EntityExtractor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a simplified version of the extraction settings for testing
        self.test_settings = {
            'minimum_entity_length': 2,
            'excluded_entities': {
                'common_words': ['the', 'and', 'for'],
                'stop_phrases': ['et al', 'figure'],
            },
            'entity_types': ['PERSON', 'ORG', 'PRODUCT']
        }
        
        # Create the entity extractor with the test settings
        self.extractor = EntityExtractor(self.test_settings)
        
        # Sample publication content
        self.sample_publication = {
            'metadata': {
                'author': 'Test Author',
                'title': 'Test Paper',
                'year': '2023',
                'basename': 'test_author_paper_2023'
            },
            'sections': [
                {
                    'title': 'Introduction',
                    'content': 'This paper discusses Machine Learning and Artificial Intelligence. John Smith from Stanford University contributed to this work.'
                },
                {
                    'title': 'Methods',
                    'content': 'We used Neural Networks and Deep Learning techniques. The Google Research team provided valuable insights.'
                }
            ],
            'vectors': [
                {
                    'vector_id': 'M1',
                    'vector_type': 'Overview',
                    'content': 'This research explores Quantum Computing and its applications in Cryptography.'
                }
            ]
        }
    
    def test_extract_entities_from_text(self):
        """Test extracting entities from text."""
        # Test with a simple text
        text = "John Smith works at Microsoft Corporation on Artificial Intelligence projects."
        entities = self.extractor._extract_entities_from_text(text)
        
        # Check that the expected entities were extracted
        self.assertIn('John Smith', entities)
        self.assertIn('Microsoft Corporation', entities)
        self.assertIn('Artificial Intelligence', entities)
        
        # Test with excluded words
        text = "The figure shows data from the experiment."
        entities = self.extractor._extract_entities_from_text(text)
        self.assertNotIn('The', entities)
        self.assertNotIn('Figure', entities)
    
    def test_extract_entities(self):
        """Test extracting entities from a publication."""
        result = self.extractor.extract_entities(self.sample_publication)
        
        # Check that the metadata was preserved
        self.assertEqual(result['metadata']['author'], 'Test Author')
        
        # Check that the expected entities were extracted
        entities = result['entities']
        self.assertIn('Machine Learning', entities)
        self.assertIn('Artificial Intelligence', entities)
        self.assertIn('John Smith', entities)
        self.assertIn('Stanford University', entities)
        self.assertIn('Neural Networks', entities)
        self.assertIn('Deep Learning', entities)
        self.assertIn('Google Research', entities)
        self.assertIn('Quantum Computing', entities)
        self.assertIn('Cryptography', entities)
        
        # Check that the entities have the correct source information
        self.assertIn('sections', entities['Machine Learning'])
        self.assertIn('sections', entities['Stanford University'])
        self.assertIn('vectors', entities['Quantum Computing'])
    
    def test_extract_entities_from_publications(self):
        """Test extracting entities from multiple publications."""
        # Create a second sample publication
        sample_publication2 = {
            'metadata': {
                'author': 'Another Author',
                'title': 'Another Paper',
                'year': '2022',
                'basename': 'another_author_paper_2022'
            },
            'sections': [
                {
                    'title': 'Introduction',
                    'content': 'This paper discusses Robotics and Computer Vision. Jane Doe from MIT contributed to this work.'
                }
            ],
            'vectors': []
        }
        
        # Extract entities from both publications
        results = self.extractor.extract_entities_from_publications([
            self.sample_publication,
            sample_publication2
        ])
        
        # Check the all_entities result
        all_entities = results['all_entities']
        self.assertIn('Machine Learning', all_entities)
        self.assertIn('Robotics', all_entities)
        self.assertIn('Jane Doe', all_entities)
        self.assertIn('MIT', all_entities)
        
        # Check that each entity has the correct publication information
        self.assertEqual(len(all_entities['Machine Learning']['publications']), 1)
        self.assertEqual(len(all_entities['Robotics']['publications']), 1)
        
        # Check the publication_entities result
        publication_entities = results['publication_entities']
        self.assertEqual(len(publication_entities), 2)
        
        # Check that each publication has the correct entities
        pub1_entities = publication_entities[0]['entities']
        pub2_entities = publication_entities[1]['entities']
        
        self.assertIn('Machine Learning', pub1_entities)
        self.assertIn('Robotics', pub2_entities)
        self.assertNotIn('Robotics', pub1_entities)
        self.assertNotIn('Machine Learning', pub2_entities)

if __name__ == '__main__':
    unittest.main() 
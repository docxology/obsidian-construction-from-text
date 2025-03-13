"""Tests for the markdown parser."""

import os
import tempfile
import unittest
from pathlib import Path

from src.parsers.markdown_parser import MarkdownParser
from src.config import PARSER_SETTINGS

class TestMarkdownParser(unittest.TestCase):
    """Test cases for the MarkdownParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = MarkdownParser(PARSER_SETTINGS)
        
        # Create a temporary test file
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.temp_dir.name, "test_author_paper_2023.md")
        
        # Sample markdown content
        self.test_content = """# Test Paper Title

__Paper Type:__ Research

## M1: System Overview
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: This is a test description of a system.
    *   CT-GIN Mapping: Test mapping
    *   Implicit/Explicit: Explicit

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: This is a test description of energy input.
"""
        
        # Write the test content to the file
        with open(self.test_file_path, 'w', encoding='utf-8') as f:
            f.write(self.test_content)
    
    def tearDown(self):
        """Tear down test fixtures."""
        self.temp_dir.cleanup()
    
    def test_parse_file(self):
        """Test parsing a single markdown file."""
        result = self.parser.parse_file(self.test_file_path)
        
        # Check metadata
        self.assertEqual(result['metadata']['author'], 'test_author')
        self.assertEqual(result['metadata']['title'], 'paper')
        self.assertEqual(result['metadata']['year'], '2023')
        self.assertEqual(result['metadata']['title_text'], 'Test Paper Title')
        self.assertEqual(result['metadata']['paper_type'], 'Research')
        
        # Check sections
        self.assertEqual(len(result['sections']), 4)
        self.assertEqual(result['sections'][0]['title'], 'M1: System Overview')
        self.assertEqual(result['sections'][1]['title'], '1.1 System Description')
        
        # Check vectors
        self.assertEqual(len(result['vectors']), 3)
        self.assertEqual(result['vectors'][0]['vector_id'], 'M1')
        self.assertEqual(result['vectors'][0]['vector_type'], 'Overview')
        self.assertEqual(result['vectors'][1]['vector_id'], 'M1.1')
        self.assertEqual(result['vectors'][1]['vector_type'], 'Description')
        self.assertEqual(result['vectors'][2]['vector_id'], 'M2')
        self.assertEqual(result['vectors'][2]['vector_type'], 'Energy')
    
    def test_parse_directory(self):
        """Test parsing a directory of markdown files."""
        # Create a second test file
        test_file2_path = os.path.join(self.temp_dir.name, "another_author_paper_2022.md")
        with open(test_file2_path, 'w', encoding='utf-8') as f:
            f.write(self.test_content)
        
        # Parse the directory
        results = self.parser.parse_directory(self.temp_dir.name)
        
        # Check that both files were parsed
        self.assertEqual(len(results), 2)
        
        # Check that the metadata was extracted correctly
        authors = [r['metadata']['author'] for r in results]
        self.assertIn('test_author', authors)
        self.assertIn('another_author', authors)
        
        years = [r['metadata']['year'] for r in results]
        self.assertIn('2023', years)
        self.assertIn('2022', years)

if __name__ == '__main__':
    unittest.main() 
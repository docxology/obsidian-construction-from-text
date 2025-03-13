"""Generate an Obsidian knowledge base from parsed publication content."""

import os
import logging
import json
from typing import Dict, List, Any, Set, Optional
from collections import defaultdict

import networkx as nx

from ..utils.file_utils import ensure_directory, save_markdown_file
from ..utils.text_utils import generate_slug, create_obsidian_link

logger = logging.getLogger(__name__)

class ObsidianGenerator:
    """
    Generate an Obsidian knowledge base from parsed publication content.
    
    Creates a structured Obsidian vault with:
    - Entity notes
    - Topic notes
    - Publication notes
    - Cross-linked references
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the ObsidianGenerator.
        
        Args:
            config: Configuration dictionary containing Obsidian settings
        """
        self.config = config
        
        # Set up paths
        self.obsidian_dir = config.get('obsidian_dir', 'obsidian')
        self.entities_folder = os.path.join(self.obsidian_dir, config.get('entities_folder', 'Entities'))
        self.topics_folder = os.path.join(self.obsidian_dir, config.get('topics_folder', 'Topics'))
        self.publications_folder = os.path.join(self.obsidian_dir, config.get('publications_folder', 'Publications'))
        self.index_filename = config.get('index_filename', 'index.md')
        
        # Create network for relationship tracking
        self.graph = nx.DiGraph()
    
    def generate_knowledge_base(self, extraction_results: Dict[str, Any]) -> bool:
        """
        Generate an Obsidian knowledge base from extraction results.
        
        Args:
            extraction_results: Results from entity and topic extraction
            
        Returns:
            True if knowledge base was generated successfully, False otherwise
        """
        logger.info(f"Generating Obsidian knowledge base in {self.obsidian_dir}")
        
        # Set up directory structure
        if not self._setup_directory_structure():
            logger.error("Failed to set up directory structure")
            return False
        
        # Extract data from results
        all_entities = extraction_results.get('entity_extraction', {}).get('all_entities', {})
        publication_entities = extraction_results.get('entity_extraction', {}).get('publication_entities', [])
        
        topics = extraction_results.get('topic_extraction', {}).get('topics', [])
        document_topics = extraction_results.get('topic_extraction', {}).get('document_topics', [])
        
        # Generate entity pages
        self._generate_entity_pages(all_entities)
        
        # Generate topic pages
        self._generate_topic_pages(topics, document_topics)
        
        # Generate publication pages
        publications = extraction_results.get('parsed_publications', [])
        self._generate_publication_pages(publications, publication_entities, document_topics)
        
        # Generate index page
        self._generate_index_page(all_entities, topics, publications)
        
        # Generate graph visualization data
        self._export_graph_data()
        
        return True
    
    def _setup_directory_structure(self) -> bool:
        """
        Set up the Obsidian directory structure.
        
        Returns:
            True if directories were created successfully, False otherwise
        """
        try:
            # Create main directories
            ensure_directory(self.obsidian_dir)
            ensure_directory(self.entities_folder)
            ensure_directory(self.topics_folder)
            ensure_directory(self.publications_folder)
            
            return True
        except Exception as e:
            logger.error(f"Failed to set up directory structure: {e}")
            return False
    
    def _generate_entity_pages(self, all_entities: Dict[str, Any]) -> None:
        """
        Generate Obsidian pages for entities.
        
        Args:
            all_entities: Dictionary of all extracted entities
        """
        logger.info(f"Generating {len(all_entities)} entity pages")
        
        for entity, info in all_entities.items():
            # Create a slug for the filename
            entity_slug = generate_slug(entity)
            filename = os.path.join(self.entities_folder, f"{entity_slug}.md")
            
            # Add node to the graph
            self.graph.add_node(f"entity:{entity_slug}", type="entity", name=entity)
            
            # Generate content
            content = f"# {entity}\n\n"
            content += f"## Overview\n\n"
            content += f"Entity extracted from {len(info.get('publications', []))} publications.\n\n"
            
            # Add publication references
            content += f"## Referenced in Publications\n\n"
            
            for pub_info in info.get('publications', []):
                metadata = pub_info.get('metadata', {})
                pub_title = metadata.get('title_text', metadata.get('title', metadata.get('basename', 'Unknown')))
                pub_slug = generate_slug(metadata.get('basename', 'unknown'))
                
                # Add edge to the graph
                self.graph.add_edge(f"entity:{entity_slug}", f"publication:{pub_slug}", type="referenced_in")
                
                # Add publication reference to the content
                content += f"- {create_obsidian_link(pub_title, f'../Publications/{pub_slug}')}\n"
                
                # Add specific occurrences if available
                occurrences = pub_info.get('occurrences', {})
                if occurrences:
                    # Add section occurrences
                    for section in occurrences.get('sections', [])[:3]:  # Limit to 3 for brevity
                        section_title = section.get('title', 'Unnamed Section')
                        content += f"  - In section: *{section_title}*\n"
                    
                    # Add vector occurrences
                    for vector in occurrences.get('vectors', [])[:3]:  # Limit to 3 for brevity
                        vector_id = vector.get('id', 'Unknown')
                        vector_type = vector.get('type', 'Unknown')
                        content += f"  - In vector: *{vector_id}* (Type: {vector_type})\n"
                    
                    # Indicate if more occurrences were omitted
                    section_count = len(occurrences.get('sections', []))
                    vector_count = len(occurrences.get('vectors', []))
                    if section_count > 3 or vector_count > 3:
                        content += f"  - *...and {section_count + vector_count - 6 if section_count + vector_count > 6 else 0} more occurrences*\n"
            
            # Save the file
            save_markdown_file(content, filename)
    
    def _generate_topic_pages(self, topics: List[Dict[str, Any]], document_topics: List[Dict[str, Any]]) -> None:
        """
        Generate Obsidian pages for topics.
        
        Args:
            topics: List of extracted topics
            document_topics: List of document-topic assignments
        """
        logger.info(f"Generating {len(topics)} topic pages")
        
        for topic in topics:
            topic_id = topic.get('id', 0)
            topic_name = topic.get('name', f"Topic {topic_id}")
            topic_description = topic.get('description', '')
            top_terms = topic.get('top_terms', [])
            
            # Create a slug for the filename
            topic_slug = generate_slug(topic_name)
            filename = os.path.join(self.topics_folder, f"{topic_slug}.md")
            
            # Add node to the graph
            self.graph.add_node(f"topic:{topic_slug}", type="topic", name=topic_name)
            
            # Generate content
            content = f"# {topic_name}\n\n"
            content += f"## Description\n\n"
            content += f"{topic_description}\n\n"
            
            # Add top terms
            content += f"## Top Terms\n\n"
            for term in top_terms:
                content += f"- {term}\n"
            
            # Add publication references
            content += f"\n## Referenced in Publications\n\n"
            
            # Find publications that contain this topic
            for doc_topic in document_topics:
                metadata = doc_topic.get('metadata', {})
                pub_title = metadata.get('title_text', metadata.get('title', metadata.get('basename', 'Unknown')))
                pub_slug = generate_slug(metadata.get('basename', 'unknown'))
                
                # Check if this document contains this topic
                for doc_topic_info in doc_topic.get('topics', []):
                    if doc_topic_info.get('topic_id') == topic_id:
                        weight = doc_topic_info.get('weight', 0)
                        
                        # Add edge to the graph
                        self.graph.add_edge(f"topic:{topic_slug}", f"publication:{pub_slug}", 
                                          type="contained_in", weight=weight)
                        
                        # Add publication reference to the content with weight
                        content += f"- {create_obsidian_link(pub_title, f'../Publications/{pub_slug}')} (Relevance: {weight:.2f})\n"
            
            # Save the file
            save_markdown_file(content, filename)
    
    def _generate_publication_pages(self, publications: List[Dict[str, Any]], 
                                  publication_entities: List[Dict[str, Any]],
                                  document_topics: List[Dict[str, Any]]) -> None:
        """
        Generate Obsidian pages for publications.
        
        Args:
            publications: List of parsed publications
            publication_entities: List of entities by publication
            document_topics: List of topics by publication
        """
        logger.info(f"Generating {len(publications)} publication pages")
        
        for publication in publications:
            metadata = publication.get('metadata', {})
            sections = publication.get('sections', [])
            vectors = publication.get('vectors', [])
            
            # Get the title and filename
            title = metadata.get('title_text', metadata.get('title', metadata.get('basename', 'Unknown')))
            pub_slug = generate_slug(metadata.get('basename', 'unknown'))
            filename = os.path.join(self.publications_folder, f"{pub_slug}.md")
            
            # Add node to the graph
            self.graph.add_node(f"publication:{pub_slug}", type="publication", name=title)
            
            # Generate content
            content = f"# {title}\n\n"
            
            # Add metadata
            content += f"## Metadata\n\n"
            content += f"- **Author:** {metadata.get('author', 'Unknown')}\n"
            content += f"- **Year:** {metadata.get('year', 'Unknown')}\n"
            content += f"- **Paper Type:** {metadata.get('paper_type', 'Unknown')}\n"
            content += f"- **Filename:** {metadata.get('filename', 'Unknown')}\n\n"
            
            # Add entities
            pub_entity_info = None
            for entity_info in publication_entities:
                if entity_info.get('metadata', {}).get('basename') == metadata.get('basename'):
                    pub_entity_info = entity_info
                    break
            
            if pub_entity_info and pub_entity_info.get('entities'):
                content += f"## Entities\n\n"
                entities = pub_entity_info.get('entities', {})
                for entity, occurrences in entities.items():
                    entity_slug = generate_slug(entity)
                    
                    # Add edge to the graph
                    self.graph.add_edge(f"publication:{pub_slug}", f"entity:{entity_slug}", type="contains")
                    
                    # Add entity to the content
                    content += f"- {create_obsidian_link(entity, f'../Entities/{entity_slug}')}\n"
            
            # Add topics
            doc_topic_info = None
            for topic_info in document_topics:
                if topic_info.get('metadata', {}).get('basename') == metadata.get('basename'):
                    doc_topic_info = topic_info
                    break
            
            if doc_topic_info and doc_topic_info.get('topics'):
                content += f"\n## Topics\n\n"
                for topic in doc_topic_info.get('topics', []):
                    topic_id = topic.get('topic_id', 0)
                    topic_name = topic.get('topic_name', f"Topic {topic_id}")
                    topic_slug = generate_slug(topic_name)
                    weight = topic.get('weight', 0)
                    
                    # Add edge to the graph
                    self.graph.add_edge(f"publication:{pub_slug}", f"topic:{topic_slug}", 
                                      type="related_to", weight=weight)
                    
                    # Add topic to the content
                    content += f"- {create_obsidian_link(topic_name, f'../Topics/{topic_slug}')} (Relevance: {weight:.2f})\n"
            
            # Add content summary
            content += f"\n## Content Summary\n\n"
            
            # Add sections
            content += f"### Sections\n\n"
            for section in sections:
                section_level = section.get('level', 2)
                section_title = section.get('title', 'Unnamed Section')
                
                level_indicator = "#" * section_level
                content += f"- {level_indicator} {section_title}\n"
            
            # Add vectors
            content += f"\n### Vectors\n\n"
            for vector in vectors:
                vector_id = vector.get('vector_id', 'Unknown')
                vector_type = vector.get('vector_type', 'Unknown')
                content += f"- **{vector_id}** (Type: {vector_type})\n"
            
            # Save the file
            save_markdown_file(content, filename)
    
    def _generate_index_page(self, all_entities: Dict[str, Any], 
                           topics: List[Dict[str, Any]], 
                           publications: List[Dict[str, Any]]) -> None:
        """
        Generate the main index page for the Obsidian vault.
        
        Args:
            all_entities: Dictionary of all extracted entities
            topics: List of extracted topics
            publications: List of parsed publications
        """
        logger.info("Generating index page")
        
        filename = os.path.join(self.obsidian_dir, self.index_filename)
        
        # Generate content
        content = f"# Publication Knowledge Base\n\n"
        
        # Add summary statistics
        content += f"## Summary\n\n"
        content += f"- **Publications:** {len(publications)}\n"
        content += f"- **Entities:** {len(all_entities)}\n"
        content += f"- **Topics:** {len(topics)}\n\n"
        
        # Add top entities by occurrence
        content += f"## Top Entities\n\n"
        top_entities = sorted(
            all_entities.items(), 
            key=lambda x: x[1].get('total_occurrences', 0), 
            reverse=True
        )[:20]  # Top 20 entities
        
        for entity, info in top_entities:
            entity_slug = generate_slug(entity)
            occurrences = info.get('total_occurrences', 0)
            num_publications = len(info.get('publications', []))
            
            content += f"- {create_obsidian_link(entity, f'Entities/{entity_slug}')} " \
                     f"({occurrences} occurrences in {num_publications} publications)\n"
        
        # Add top topics
        content += f"\n## Topics\n\n"
        sorted_topics = sorted(topics, key=lambda x: x.get('weight', 0), reverse=True)
        
        for topic in sorted_topics:
            topic_name = topic.get('name', f"Topic {topic.get('id', 0)}")
            topic_slug = generate_slug(topic_name)
            description = topic.get('description', '')
            
            content += f"- {create_obsidian_link(topic_name, f'Topics/{topic_slug}')} - {description}\n"
        
        # Add recent publications
        content += f"\n## Recent Publications\n\n"
        recent_publications = sorted(
            publications, 
            key=lambda x: x.get('metadata', {}).get('year', '0'), 
            reverse=True
        )[:20]  # Top 20 recent publications
        
        for publication in recent_publications:
            metadata = publication.get('metadata', {})
            title = metadata.get('title_text', metadata.get('title', metadata.get('basename', 'Unknown')))
            pub_slug = generate_slug(metadata.get('basename', 'unknown'))
            year = metadata.get('year', 'Unknown')
            author = metadata.get('author', 'Unknown')
            
            content += f"- {create_obsidian_link(title, f'Publications/{pub_slug}')} " \
                     f"({author}, {year})\n"
        
        # Save the file
        save_markdown_file(content, filename)
    
    def _export_graph_data(self) -> None:
        """
        Export the knowledge graph data for visualization.
        """
        logger.info("Exporting graph data")
        
        filename = os.path.join(self.obsidian_dir, "graph_data.json")
        
        # Convert graph to JSON serializable format
        nodes = []
        for node, attrs in self.graph.nodes(data=True):
            nodes.append({
                "id": node,
                "type": attrs.get("type", "unknown"),
                "name": attrs.get("name", node)
            })
        
        edges = []
        for source, target, attrs in self.graph.edges(data=True):
            edges.append({
                "source": source,
                "target": target,
                "type": attrs.get("type", "unknown"),
                "weight": attrs.get("weight", 1.0)
            })
        
        graph_data = {
            "nodes": nodes,
            "edges": edges
        }
        
        # Save the graph data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(graph_data, f, indent=2) 
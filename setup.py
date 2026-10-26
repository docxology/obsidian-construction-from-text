#!/usr/bin/env python
"""Setup script for the Publication Parser and Obsidian Knowledge Base Generator."""

from setuptools import setup, find_packages
import os

# Read the contents of the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# Get version from src/__init__.py
with open(os.path.join("src", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

setup(
    name="publication-parser",
    version=version,
    description="Parse publications and generate an Obsidian knowledge base",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Publication Parser Team",
    url="https://github.com/docxology/obsidian-construction-from-text",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "publication-parser=src.cli:main",
        ],
    },
) 
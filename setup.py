"""
Setup configuration for Ternary Moral Logic (TML) package
Author: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Ternary Moral Logic: A framework for ethical AI decision-making"

# Read requirements from requirements.txt if it exists
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="ternary-moral-logic",
    version="1.0.0",
    author="Lev Goukassian",
    author_email="leogouk@gmail.com",
    description="A framework for implementing ethical hesitation and moral reasoning in AI systems",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/FractonicMind/TernaryMoralLogic",
    project_urls={
        "Bug Reports": "https://github.com/FractonicMind/TernaryMoralLogic/issues",
        "Source": "https://github.com/FractonicMind/TernaryMoralLogic",
        "Documentation": "https://github.com/FractonicMind/TernaryMoralLogic/tree/main/docs",
        "Research Paper": "https://github.com/FractonicMind/TernaryMoralLogic/tree/main/theory",
    },
    packages=find_packages(include=['tml', 'tml.*']),
    package_dir={'': 'implementations/python-library'},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Education",
        "Topic :: Sociology",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
            "pre-commit>=2.15",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.15",
        ],
        "examples": [
            "jupyter>=1.0",
            "matplotlib>=3.3",
            "pandas>=1.3",
            "seaborn>=0.11",
        ]
    },
    entry_points={
        "console_scripts": [
            "tml-evaluate=tml.cli:main",
            "tml-demo=tml.examples:run_demo",
        ],
    },
    include_package_data=True,
    package_data={
        "tml": ["data/*.json", "templates/*.txt"],
    },
    zip_safe=False,
    keywords=[
        "artificial intelligence",
        "ethics",
        "moral reasoning", 
        "decision making",
        "ternary logic",
        "AI safety",
        "machine ethics",
        "value alignment",
        "ethical AI",
        "moral AI"
    ],
    license="MIT",
    platforms=["any"],
    
    # Additional metadata for academic use
    options={
        "bdist_wheel": {
            "universal": False,
        }
    },
    
    # Research and citation information
    metadata={
        "orcid": "0009-0006-5966-1243",
        "research_area": "AI Ethics and Moral Reasoning",
        "citation": "Goukassian, L. (2025). Ternary Moral Logic: Implementing Ethical Hesitation in AI Systems. AI and Ethics (under review).",
        "funding": "Independent Research",
        "legacy_note": "This framework represents Lev Goukassian's contribution to ethical AI, created during his final months as a gift to humanity's future."
    }
)

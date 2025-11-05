import sys
from pathlib import Path

# Add path to your source code
root_path = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_path.absolute()))

project = 'My Python Project'
copyright = '2025, Your Name'
author = 'Your Name'
release = '1.0.0'

# Add extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []

# Change theme
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Add source suffix
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
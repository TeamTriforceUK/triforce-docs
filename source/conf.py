import sys
import os
import sphinx_rtd_theme

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

extensions = [
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'Triforce'
copyright = u'2017, Cameron A. Craig'
author = u'Cameron A. Craig'
version = u'0.1.0'
release = u'0.1.0'
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False

if not on_rtd:
    # Use the RTD theme explicitly if it is available
    try:
        import sphinx_rtd_theme
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
        html_theme = "sphinx_rtd_theme"
    except ImportError:
        pass

html_static_path = ['_static']
htmlhelp_basename = 'triforcedoc'


latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'triforce.tex', u'triforce Documentation',
     u'Cameron A. Craig', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'triforce', u'Triforce Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'triforce', u'Triforce Documentation',
     author, 'triforce', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

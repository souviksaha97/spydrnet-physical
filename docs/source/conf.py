# -*- coding: utf-8 -*-
# pylint: skip-file
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import pathlib
sys.path.insert(0, os.path.abspath('../..'))  # nopep8
import spydrnet as sdn
import spydrnet_physical as sdnphy
from sphinx_gallery.sorting import ExplicitOrder
from sphinx_gallery.sorting import FileNameSortKey


# -- Project information -----------------------------------------------------

project = 'SpyDrNet-Physical'
copyright = '2021, University of Utah'
author = 'The Laboratory for NanoIntegrated Systems (LNIS)'

# The short X.Y version
version = sdnphy.__version__
# The full version, including alpha/beta/rc tags
release = sdnphy.__release__

numfig = True


# -- General configuration --

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.programoutput',
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib_hdl_diagrams',
    'sphinx_gallery.gen_gallery',
]


# generate autosummary pages
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of prefixs that are ignored when creating the module index. (new in Sphinx 0.6)
modindex_common_prefix = ["spydrnet_physical."]

# doctest_global_setup = "import spydrnet_physical as sdnphy"

# treat ``x, y : type`` as vars x and y instead of default ``y(x,) : type``
napoleon_use_param = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'


# Adding custom CSS stylesheet
html_css_files = [
    'custom.css',
]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SpyDrNet-Physical'
verilog_diagram_yosys = "system"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'H',

    # Oneside (remove blank pages)
    #
    'extraclassoptions': 'openany,oneside'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('reference/index', 'spydrnet_reference.tex', 'SpyDrNet Reference',
     'BYU Configurable Computing Lab', 'manual'),
]

latex_appendices = ['tutorial']

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'spydrnet', 'SpyDrNet Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, 'SpyDrNet', 'SpyDrNet-Physical Documentation',
#     author, 'SpyDrNet-Physical', 'One line description of project.',
#      'Miscellaneous'),
# ]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

rst_epilog = """
.. |sdphy| replace:: SpyDrNet-Physical
"""

sphinx_gallery_conf = {
    # path to your example scripts
    'examples_dirs': [
        os.path.join('..', '..', 'examples', 'basic'),
        os.path.join('..', '..', 'examples', 'OpenFPGA')
    ],
    # path to where to save gallery generated output
    'gallery_dirs': ['auto_basic', "auto_openfpga"],
    'remove_config_comments': True,
    'filename_pattern': '/*.py',
    'capture_repr': (),
    'within_subsection_order': FileNameSortKey,
    'subsection_order': ExplicitOrder(['../../examples/basic',
                                       '../../examples/OpenFPGA',
                                       '../../examples/OpenFPGA/basic',
                                       '../../examples/OpenFPGA/clock_tree',
                                       '../../examples/OpenFPGA/config_chain',
                                       '../../examples/OpenFPGA/rendering',
                                       '../../examples/OpenFPGA/partition']),
}


def CollectRst():
    verilog_dir = os.path.join(
        '..', '..', 'spydrnet_physical', 'support_files', 'sample_verilog')
    out_dir = os.path.join("auto_sample_verilog")
    pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)
    index_fp = open(os.path.join(out_dir, "index.rst"), "w")
    index_fp.write("Sample Verilog Netlists\n=======================" +
                   "\n\n.. toctree::\n   :glob:\n   :maxdepth: 2\n\n   ./*")
    for subdir, dirs, files in os.walk(verilog_dir):
        for file in files:
            if file.endswith(".v"):
                basename = os.path.splitext(os.path.basename(file))[0]
                filename = os.path.join(subdir, file)
                print(f"subdir {subdir}")
                print(f"file {file}")
                print(f"basename {basename}")
                print(f"out_dir {out_dir}")
                print(f"filename {filename}")
                print(os.path.join(out_dir, file+".rst"))
                print()
                with open(os.path.join(out_dir, basename+".rst"), "w") as fp:
                    fp.write(
                        f'{basename}\n' +
                        f'=================\n\n' +
                        f'.. hdl-diagram:: ../{filename}\n' +
                        f'   :type: netlistsvg\n' +
                        f'   :align: center\n' +
                        f'\n\n' +
                        f'.. literalinclude:: ../{filename}\n' +
                        f'   :language: verilog\n'
                    )
    index_fp.close()


CollectRst()

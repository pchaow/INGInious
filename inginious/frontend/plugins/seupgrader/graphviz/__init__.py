# -*- coding: utf-8 -*-
"""
    Graphviz Dot directive
"""

from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives

import docutils_graphviz

def init(plugin_manager, _, _2, _3):
    """ Init the plugin """
    directives.register_directive('dot', docutils_graphviz.Graphviz)

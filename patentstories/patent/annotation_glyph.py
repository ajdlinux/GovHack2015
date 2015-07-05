# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'

from collections import defaultdict

ANNOTATION_GLYPH_SET = defaultdict(lambda: ('info', 'glyphicon-question-sign'))

__GLYPH_SET__ = {

    'Link': ('glyphicon-link', 'info'),
    'Picture': ('glyphicon-picture', 'info'),
    'Comment': ('glyphicon-comment', 'info'),
    'News Article': ('glyphicon-list-alt', 'info'),
    'Summary': ('glyphicon-list-alt', 'info'),

}

for k,v in __GLYPH_SET__.items():
    ANNOTATION_GLYPH_SET[k] = v

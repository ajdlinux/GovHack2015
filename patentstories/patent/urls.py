# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'
from django.conf.urls import url
from .views import view_patent, add_annotation, search_patent

urlpatterns = [
    url(r'^$', search_patent, name='search_patent'),
    url(r'^(?P<patent_id>\w{10})/$', view_patent, name='patent'),
    url(r'^(?P<patent_id>\w{10})/annotate/$', add_annotation, name='add_annotation'),
]

# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'
from django.conf.urls import url
from .views import view_patent

urlpatterns = [
    url(r'^(?P<patent_id>\w{10})/$', view_patent, name='patent'),
]

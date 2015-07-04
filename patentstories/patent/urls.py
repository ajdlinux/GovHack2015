# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'
from django.conf.urls import url
from .views import dummy_patent

urlpatterns = [
    url(r'^(?P<patent_id>\d{10})/$', dummy_patent, name='patent'),
]

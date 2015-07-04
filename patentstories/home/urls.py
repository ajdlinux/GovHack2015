# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]

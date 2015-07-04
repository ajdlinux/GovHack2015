# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'

from django import forms
from .models import PatentAnnotation, PatentAnnotationTypes

class AddAnnotationForm(forms.Form):
    annotation_type = forms.ChoiceField(choices=PatentAnnotationTypes.choices)
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    link = forms.URLField()
    link_other = forms.CharField(max_length=100)
    date = forms.DateField()

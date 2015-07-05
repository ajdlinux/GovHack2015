# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'

from django import forms
from .models import PatentAnnotation, PatentAnnotationTypes

class AddAnnotationForm(forms.Form):
    annotation_type = forms.ChoiceField(choices=PatentAnnotationTypes.choices)
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea, required=False)
    link = forms.URLField(required=False)
    #link_other = forms.CharField(max_length=100)
    date = forms.DateField(required=False)
    image = forms.ImageField(required=False)
    image_alt = forms.CharField(max_length=100, required=False)

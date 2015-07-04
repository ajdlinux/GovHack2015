# -*- coding: utf-8 -*-

__author__ = 'Andrew Donnellan'

from django import forms
from .models import PatentAnnotation, PatentAnnotationTypes

class AddAnnotationForm(forms.Form):
    annotation_type = forms.ChoiceField(choices=PatentAnnotationTypes.choices)

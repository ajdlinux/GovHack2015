from django.contrib import admin
from .models import PatentAnnotation, PatentApplication

admin.site.register(PatentAnnotation)
admin.site.register(PatentApplication)

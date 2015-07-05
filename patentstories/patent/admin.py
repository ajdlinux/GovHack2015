from django.contrib import admin
from .models import PatentAnnotation, PatentApplication, FeaturedStory, ExternalCachedData

admin.site.register(PatentAnnotation)
admin.site.register(PatentApplication)
admin.site.register(FeaturedStory)
admin.site.register(ExternalCachedData)

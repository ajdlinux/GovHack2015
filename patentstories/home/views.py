from django.shortcuts import render
from patent.models import FeaturedStory

def home(request):
    featured = FeaturedStory.objects.filter(enabled=True).order_by('?')[:4]
    return render(request, 'home/home.html', {'featured': featured})

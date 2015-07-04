from django.shortcuts import render

# Create your views here.


def dummy_patent(request, patent_id):
    context = {}
    return render(request, 'patent/patent.html', context)

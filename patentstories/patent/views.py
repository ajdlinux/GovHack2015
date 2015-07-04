from django.shortcuts import render

# Create your views here.


def dummy_patent(request, patent_id):
    patent = {'patent_id': patent_id, 'description': 'A patent on a really cool thing'}
    context = {'patent': patent}
    return render(request, 'patent/patent.html', context)

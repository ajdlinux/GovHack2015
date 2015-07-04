from django.shortcuts import render

# Create your views here.


def dummy_patent(request, patent_id):
    patent = {'patent_id': patent_id.upper(), 'description': 'A patent on a really cool thing'}
    timeline = [{
        'title': 'bananas on toast',
        'date': '25th September 2014',
    }, None, None, None, None]
    context = {'patent': patent, 'timeline': timeline}
    return render(request, 'patent/patent.html', context)

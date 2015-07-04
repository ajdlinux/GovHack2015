from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import PatentApplication, PatentAnnotation
from .mongo_adapters.event_glyph import EVENT_GLYPH_SET
from .forms import AddAnnotationForm

def view_patent(request, patent_id):
    """
    View to display patent timeline for a given patent application ID.

    :param request: Django request object
    :param patent_id: patent application number
    :return: Django response object
    """

    try:
        patent_application = PatentApplication.objects.get(australian_appl_no=patent_id)
    except PatentApplication.DoesNotExist:
        patent_application = PatentApplication(australian_appl_no=patent_id)
        event_timeline = patent_application.get_event_timeline()
        if event_timeline:
            # patent has been found in IPGOD
            patent_application.save()
        else:
            raise Exception # TODO fix this

    patent_data = patent_application.get_patent_data()
    glyphify(patent_data['timeline'])
    return render(request, 'patent/patent.html', patent_data)


def add_annotation(request, patent_id):
    """
    View to process annotation form
    :param request: Django request object
    :param patent_id: patent application number
    :return: Django response object
    """
    if request.method == 'POST':
        form = AddAnnotationForm(request.POST)
        if form.is_valid():
            annotation = PatentAnnotation()
            annotation.patent_application = PatentApplication.objects.get(pk=patent_id)
            annotation.annotation_type = request.POST['annotation_type']
            annotation.body = request.POST['body']
            annotation.date = request.POST['date']
            annotation.link = request.POST['link']
            annotation.link_other = request.POST['link_other']

            annotation.save()
            return HttpResponseRedirect(reverse('patent', args=(patent_id,)))
    else:
        form = AddAnnotationForm()
    return render(request, 'patent/add_annotation.html', {'form': form})


def dummy_patent(request, patent_id):
    patent = {'patent_id': patent_id.upper(), 'description': 'A patent on a really cool thing'}
    timeline = [{
        'title': 'bananas on toast',
        'date': '25th September 2014',
    }, None, None, None, None]
    context = {'patent': patent, 'timeline': timeline}
    return render(request, 'patent/patent.html', context)

def glyphify(timeline):
    """
    Add glyph annotations to timeline items
    :param timeline: timeline object
    :type: list
    """
    for event in timeline:
        if 'event_type' in event:
            glyph, catagory = EVENT_GLYPH_SET[event["event_type"]]
            event["glyph"] = glyph
            event["catagory"] = catagory

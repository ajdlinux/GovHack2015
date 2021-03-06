import datetime
from django.conf import settings
from django.db import models
from django_enumfield import enum
from jsonfield import JSONField
from .mongo_adapters import MONGO_PATENT_EVENT_ADAPTERS
from .external_adapters import EXTERNAL_PATENT_EVENT_ADAPTERS

class PatentApplication(models.Model):
    """
    Top level type for patent applications. Acts as both a Django model and MongoDB lookup.
    """
    australian_appl_no = models.CharField(primary_key=True, max_length=10)
    def get_event_timeline(self):
        """
        Build or return the chronological timeline of Patent Application events
        :return: list of event objects
        :rtype: list
        """
        
        # Check for cached copy
        #TODO memcache/mongodb/redis this if slow
        if "timeline" in self.__dict__ and len(self.timeline) is not 0:
            return self.timeline

        if self.australian_appl_no is None:
            raise LookupError("No application number set for PatentApplication")

        self.timeline = []

        # run the mongo data adapters to organise the timeline
        for mongo_adapter in MONGO_PATENT_EVENT_ADAPTERS:
            entry = mongo_adapter(self.australian_appl_no)

            # Entry must exist
            if not entry.exists():
                continue

            entry_events = entry.get_events()
            self.timeline.extend(entry_events)

        #sort by date
        self.timeline.sort(key=lambda x: x["date"])

        return self.timeline

    def get_external_data(self):
        external_data = {}
        for external_adapter_code, external_adapter in EXTERNAL_PATENT_EVENT_ADAPTERS.items():
            try:
                cached = ExternalCachedData.objects.get(patent_application=self, adapter_code=external_adapter_code)
                external_data[external_adapter_code] = cached.data
            except ExternalCachedData.DoesNotExist:
                if external_adapter_code == 'trove':
                    title = external_data['auspat'].get('title', '')
                    applicant = external_data['auspat'].get('applicant', '')
                    inventors = external_data['auspat'].get('inventors', [])

                    external_data[external_adapter_code] = external_adapter(self, title, applicant, *inventors).get_items()

                else:
                    external_data[external_adapter_code] = external_adapter(self).get_items()
                cached = ExternalCachedData(patent_application=self, adapter_code=external_adapter_code)
                cached.data = external_data[external_adapter_code]
                cached.save()
            if type(external_data[external_adapter_code]) == dict and not any(external_data[external_adapter_code].values()):
                del external_data[external_adapter_code]
        return external_data

    def get_patent_data(self):
        """
        Build a dictionary with a combined timeline consisting of the events from the IPGOD database and the user
        annotations, and data fields from external sources
        :return: dictionary containing patent data
        :rtype: dict
        """
        patent_data = {'patent': self, 'timeline': self.get_event_timeline()}
        annotations = self.patentannotation_set.all()
        for annotation in annotations:
            #if annotation.date:
            patent_data['timeline'].append({
                'annotation_type': PatentAnnotationTypes.label(annotation.annotation_type),
                'date': annotation.date,
                'creator': annotation.creator,
                'title': annotation.title,
                'body': annotation.body,
                'link': annotation.link,
                'link_other': annotation.link_other,
                'image': annotation.image,
                'image_alt': annotation.image_alt,
            })
        patent_data['timeline'].sort(key=lambda x: x['date'] if x['date'] else datetime.date.min)

        """
        for annotation in annotations:
            if not annotation.date:
                patent_data[PatentAnnotationTypes.label(annotation.annotation_type)] = {
                    'annotation_type': PatentAnnotationTypes.label(annotation.annotation_type),
                    'date': annotation.date,
                    'creator': annotation.creator,
                    'title': annotation.title,
                    'body': annotation.body,
                    'link': annotation.link,
                    'link_other': annotation.link_other,
                    'image': annotation.image,
                    'image_alt': annotation.image_alt,
                }
        """
        external_data = self.get_external_data()
        for external_adapter_code, external_data in external_data.items():
            patent_data[external_adapter_code] = external_data

        return patent_data

    def __repr__(self):
        return u'Patent application #{0}'.format(self.australian_appl_no)


class PatentAnnotationTypes(enum.Enum):
    """
    Enum specifying types for annotations
    """
    SUMMARY = 0
    NEWS = 1
    COMMENT = 2
    PICTURE = 3
    LINK = 4

    labels = {
        SUMMARY: 'Summary',
        NEWS: 'News Article',
        COMMENT: 'Comment',
        PICTURE: 'Picture',
        LINK: 'Link',
    }

class PatentAnnotation(models.Model):
    """
    Annotations for patent applications
    """
    patent_application = models.ForeignKey('PatentApplication')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    annotation_type = enum.EnumField(PatentAnnotationTypes)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    link_other = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='annotation/', blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)


class FeaturedStory(models.Model):
    """
    Details of a featured story on the front page
    """
    patent_application = models.ForeignKey('PatentApplication')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured/')
    image_alt = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)

class ExternalCachedData(models.Model):
    """
    Cache details from external data source
    """
    patent_application = models.ForeignKey('PatentApplication')
    adapter_code = models.CharField(max_length=16)
    data = JSONField()

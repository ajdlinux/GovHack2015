import datetime
from django.conf import settings
from django.db import models
from django_enumfield import enum
from .mongo_adapters import MONGO_PATENT_EVENT_ADAPTERS

class PatentApplication(models.Model):
    """
    Top level type for patent applications. Acts as both a Django model and MongoDB lookup.
    """
    australian_appl_no = models.IntegerField(primary_key=True)
    def get_event_timeline(self):
        """
        Build or return the chronological timeline of Patent Application events
        :return: list of event objects
        :rtype: list
        """
        
        # Check for cached copy
        #TODO memcache/mongodb/redis this if slow
        if "timeline" in self.__dict__:
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

    def get_combined_timeline(self):
        """
        Build a combined timeline consisting of the events from the IPGOD database and the user annotations.
        :return: list of event objects
        :rtype: list
        """
        timeline = self.get_event_timeline()
        annotations = self.patentannotation_set.all()
        for annotation in annotations:
            timeline.append({
                'event': PatentAnnotationTypes.label(annotation.annotation_type),
                'date': annotation.date,
                'creator': annotation.creator,
                'title': annotation.title,
                'body': annotation.body,
                'link': annotation.link,
                'link_other': annotation.link_other,
            })
        timeline.sort(key=lambda x: x['date'] if x['date'] else datetime.datetime.min)
        return timeline


class PatentAnnotationTypes(enum.Enum):
    """
    Enum specifying types for annotations
    """
    SUMMARY = 0
    NEWS = 1
    COMMENT = 2
    PICTURE = 3

    labels = {
        SUMMARY: 'Summary',
        NEWS: 'News Article',
        COMMENT: 'Comment',
        PICTURE: 'Picture',
    }

class PatentAnnotation(models.Model):
    """
    Annotations for patent applications
    """
    patent_application = models.ForeignKey('PatentApplication')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    annotation_type = enum.EnumField(PatentAnnotationTypes)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    link_other = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

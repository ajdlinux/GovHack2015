from django.db import models
from .mongo_events import MONGO_PATENT_EVENT_ADAPTERS

# Create your models here.

class PatentApplication(models.Model):
    """
    Top level type for patent applications. Acts as both a Django model and MongoDB lookup.
    """
    australian_appl_no = models.IntegerField()
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
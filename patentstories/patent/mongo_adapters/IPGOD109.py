__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

# Can get opponent from seperate table
EVENT_FIELDS = {
    'published':    ("Innovation Patent Certification Published", []),
    'sealed':    ("Innovation Patent Certification Sealed", []),
    'certification':    ("Innovation Patent Certified", []),
}

class IPGOD109Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD109Adapter, self).__init__("IPGOD109", patent_application_no)


    def get_events(self):
        """
        Get events available in IPGOD109 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)



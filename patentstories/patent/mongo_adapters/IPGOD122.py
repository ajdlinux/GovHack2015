__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

# Can get opponent from seperate table
EVENT_FIELDS = {
    'application_filed':      ("Application for Restoration Filed", ["status_type"]),
    'application_published':  ("Application for Restoration Published", []),
    'opposition_filed':       ("Opposition to Restoration Filed", []),
    'opposition_decision':    ("Decision on Restoration Opposition Reached", ["opposition_decision_type"]),
    'restoration':            ("Patent Restoration", []),
    'published':              ("Restoration Published", []),

}

class IPGOD122Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD122Adapter, self).__init__("IPGOD122", patent_application_no)


    def get_events(self):
        """
        Get events available in IPGOD122 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)



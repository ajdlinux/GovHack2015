__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

# Can get opponent from seperate table
EVENT_FIELDS = {
    'applied':      ("Applied for Early Termination", []),
    'published':    ("Early Termination Decision Published", ["application_status_type", "reason_description"]),
}

class IPGOD127Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD127Adapter, self).__init__("IPGOD127", patent_application_no)


    def get_events(self):
        """
        Get events available in IPGOD127 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)



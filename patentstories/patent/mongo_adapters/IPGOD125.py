__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

# Can get opponent from seperate table
EVENT_FIELDS = {
    'request_filed':        ("Change of Ownership Details Filed", ["change_reason_type", "document_description"]),
    'name_change':          ("Ownership Details Changed", []),
    'advertised':           ("Change of Ownership Published", []),
    'asssignment_validated':("Ownership Details Validated", []),
}

class IPGOD125Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD125Adapter, self).__init__("IPGOD125", patent_application_no)


    def get_events(self):
        """
        Get events available in IPGOD125 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)



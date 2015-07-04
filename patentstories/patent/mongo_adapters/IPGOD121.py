__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

# Can get opponent from seperate table
EVENT_FIELDS = {
    'extension_from':       ("Extension of Term", ["extension_status_type"]),
    'tga_approval':         ("Earliest Therapeutic Goods Administration (TGA) Approval", ["pharmaceutical_type"]),
    'expiry':               ("Expiry following Extension of Term", []),
    'application_receipt':  ("Application for Extension of Term Received", []),
    'receipt_published':    ("Application for Extension of Term Published", []),
    'acceptance_receipt':   ("Acceptance of Extension of Term", []),
    'acceptance_published': ("Acceptance of Extension of Term Published", []),
    'opposition_filed':     ("Opposition to Extension of Term Filed", ["opposition_allowed_status"]),
    'opposition_decision':  ("Opposition to Extension of Term Decided", []),
    'refusal':              ("Extension of Term Refused", []),
    'refusal_published':    ("Refusal of Extension of Term Published", []),
    'withdrawl':            ("Extension of Term Application Withdrawn", []),
    'withdrawl_published':  ("Withdrawal of Extension of Term Application Published", []),
    'granted':              ("Extension of Term Granted", []),
    'grant_published':      ("Granting of Extension of Term Published", [])
}

class IPGOD121Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD121Adapter, self).__init__("IPGOD121", patent_application_no)


    def get_events(self):
        """
        Get events available in IPGOD121 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)



__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

# Can get opponent from seperate table
EVENT_FIELDS = {
    'last_opposition_lodge':    ("Opposition Lodgements Due", []),
    'notice_filed':             ("Opposition Lodged", []),
    'notice_served':            ("Opposition Served", []),
    'journal_published':        ("Published in Journal", ["journal_name"]),
    'grounds_statement_due':    ("Grounds for Opposition Due", []),
    'grounds_statement_filed':  ("Groups for Opposition Filed", []),
    'grounds_statement_served': ("Grounds for Opposition Served", []),
    'support_evidence_due':     ("Supporting Evidence for Opposition Due", []),
    'support_evidence_filed':   ("Supporting Evidence Filed", []),
    'support_evidence_served':  ("Supporting Evidence Served", []),
    'answer_evidence_due':      ("Opposition Answer Evidence Due", []),
    'answer_evidence_filed':    ("Opposition Answer Evidence Filed", []),
    'answer_evidence_served':   ("Opposition Answer Evidence Served", []),
    'intent_notice_due':        ("Notice of Opposition Intention Due", []),
    'intent_notice_filed':      ("Notice of Opposition Filed", []),
    'intent_notice_served':     ("Notice of Opposition Served", []),
    'reply_evidence_due':       ("Evidence in Reply Due", []),
    'reply_evidence_filed':     ("Evidence in Reply Filed", []),
    'reply_evidence_served':    ("Evidence in Reply Served", []),
    'acceptance_advertised':    ("Acceptance Advertised", []),
    'filing':                   ("Application Filed", []),
    'opi':                      ("Open to Public Inspection (OPI)", []),
    'npe':                      ("National Phase Entered", []),
    'hearing':                  ("Hearing", ["hearing_type", "location_name"]),
    'decision_issued':          ("Decision Issued", ["result_type"]),
}

class IPGOD108Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD108Adapter, self).__init__("IPGOD108", patent_application_no, pk_name='"APPLICATION_NUMBER"')


    def get_events(self):
        """
        Get events available in IPGOD108 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)



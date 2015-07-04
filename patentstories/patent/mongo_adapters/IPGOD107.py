__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

#field -> (nice-desc, [info fields])
EVENT_FIELDS= {
    "filing":                   ("Application Filed", []),
    "search_completed":         ("Search Completed", []),
    "search_results_received":  ("Search Results Received", []),
    "exam_request":             ("Examination Requested", ["exam_status_type"]),
    "exam_request_filing":      ("Examination Request Filed", ["requested_exam_type"]),
    "deferement_request":       ("Deferement Requested", []),
    "first_report_issue":       ("First Examination Report Issued", []),
    "further_report_issue":     ("Further Examination Report Issued", []),
    "search_results_received":  ("Search Results Received", []),
    "third_prty_exam_requested":("Third Party Examination Requested", []),
    "earliest_priority":        ("Earliest Priority", []),
    "acceptance_published":     ("Acceptance Published", []),
    "wipo_publication":         ("Published by World Intellectual Property Organization", []),
    "effective_patent":         ("Patent is Effective", []),
    "npe":                      ("National Phase Entered", []),
    "opi":                      ("Open to Public Inspection (OPI)", []),
    "opi_published_in_journal": ("OPI Published in Journal", []),
    "continue_renew_fee_paid":  ("Renewal Fee Due", []),
    "in_force_to":              ("No Longer Enforced", [])
}

class IPGOD107Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD107Adapter, self).__init__("IPGOD107", patent_application_no)

    def get_events(self):
        """
        Get events available in IPGOD107 entry
        :return: list of events:rtype: list
        """
        return self.process_events_list(EVENT_FIELDS)

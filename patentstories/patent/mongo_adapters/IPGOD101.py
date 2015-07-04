__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .MongoAdapter import MongoAdapter

class IPGOD101Adapter(MongoAdapter):

    def __init__(self, patent_application_no):
        super(IPGOD101Adapter,self ).__init__("IPGOD101", patent_application_no)

    def get_events(self):
        """
        Return the application date of the patent
        :return: list of event objects
        :rtype: list
        """
        return [{
            "event": "Application",
            "date": self.get_event_date("application"),
        }]

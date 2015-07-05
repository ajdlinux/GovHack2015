__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from .ExternalAdapter import ExternalAdapter
from preprocessing.settings import TROVE_KEY
from bs4 import BeautifulSoup
import requests

TROVE_ZONES = ["picture", "newspaper", "article"] #People have no relevance
TROVE_ROOT = "http://api.trove.nla.gov.au/result"
TROVE_RELEVANCE = "very relevant"
TROVE_ZONE_FILTER = lambda z: z["name"] in TROVE_ZONES
TROVE_RELEVANCE_FILTER = lambda w: w.relevance.text == TROVE_RELEVANCE
TROVE_RECORD_TAKE = 3

class TroveAdapter(ExternalAdapter):
    def __init__(self, parent_patent, *from ):
        """
        :param parent_patent: parent patent model
        :type parent_patent: PatentApplication
        :return:
        """
        super(TroveAdapter, self).__init__(parent_patent)
        self.params = {"key": TROVE_KEY}
        self.search_terms = args
        self.items = None


    def get_items(self):
        """
        Retrieve the data from the external source and returns the entires in a dict
        Is responsible for saving the corresponding models
        :return: dict of items
        :rtype: dict
        """
        #TODO implement caching here
        if self.items is None:
            self.items = {zone: [] for zone in TROVE_ZONES}
            # Query for each
            for term in self.search_terms:
                for zone, items in self.__trove_query__(term).items():
                    self.items[zone].extend(items)

        return self.items


    def __trove_query__(self, search_term):

        #initialise local params and copy instance level ones
        params = {}
        for k,v in self.params.items():
            params[k] = v

        # Set query
        params["q"] = search_term

        items = {zone: [] for zone in TROVE_ZONES}

        # Do query per zone
        for zone in TROVE_ZONES:
            params["zone"] = zone
            response = requests.get(TROVE_ROOT, params=params)

            # Check correct
            if not response.ok:
                continue

            # Parse xml response
            bss = BeautifulSoup(response.text, features="xml")
            records = bss.find("zone").records

            # Get first 3 relevant results
            for work in list(filter(TROVE_RELEVANCE_FILTER, records))[:TROVE_RECORD_TAKE]:
                items[zone].append({
                    "title": work.title.text,
                    "url": work.troveUrl.text,
                })

        return items



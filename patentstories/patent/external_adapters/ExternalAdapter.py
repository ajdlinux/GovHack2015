__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from ..models import PatentApplication

class ExternalAdapter():

    def __init__(self, parent_patent):
        """
        :param parent_patent:
        :type parent_patent: PatentApplication
        :return:
        """
        self.patent = parent_patent

    def get_items(self):
        """
        Retrieve the data from the external source and returns the entires in a list
        Is responsible for saving the corresponding models
        :return: list of items
        :rtype: list
        """
        pass
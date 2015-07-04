__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from preprocessing.MongoSingleton import MongoSingleton
from datetime import datetime

PK_NAME = "australian_appl_no"

class MongoPatentEventAdapter():

    def __init__(self, collection, patent_application_no):
        """

        :param collection: collection/database of event object
        :type: str
        :param patent_application_no: application number
        :type: int
        :return:
        """
        self.__collection__ = MongoSingleton.get_db()[collection]
        #TODO is PK actually a unique key?
        self.__record__ = self.__collection__.find_one({PK_NAME: str(patent_application_no)})

    def exists(self):
        """
        Check if record existed in MongoDB
        :return: event exists
        :rtype: bool
        """

        return self.__record__ is not None

    def get_collection_name(self):
        """
        Get the name of the event object's collection
        :return: name of collection
        :rtype: str
        """
        return self.__collection__

    def get_patent_application_no(self):
        """
        Get the patent application number of the event object
        :return: patent no
        :rtype: int
        """
        return self.__record__[PK_NAME]

    def get_mongo_record(self):
        """
        Get the record of the event object from mongodb
        :return: event record
        :rtype: dict
        """
        return self.__record__

    def get_event_date(self, event_name):
        """
        Return the date of an event in the record
        :param event_name: name of event
        :return: date of event
        :rtype: datetime
        """
        event_key = "{0}_date".format(event_name)

        # jump out if bad record or missing event
        if not self.exists() or event_key not in self.__record__:
            return None

        date_str = self.__record__[event_key]
        return datetime.strptime(date_str, "%m/%d/%Y")

    def get_events(self):
        """
        Get the events specified by the record
        :return: list of event dictionaries
        :rtype: list
        """
        pass

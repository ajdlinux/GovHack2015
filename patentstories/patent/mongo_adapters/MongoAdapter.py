__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from preprocessing.MongoSingleton import MongoSingleton
from datetime import datetime


class MongoAdapter():
    DATE_NOT_AVAILABLE = datetime.strptime("12/31/2999","%m/%d/%Y")


    def __init__(self, collection, patent_application_no, **kwargs):
        """

        :param collection: collection/database of event object
        :type: str
        :param patent_application_no: application number
        :type: str
        :return:
        """

        if "pk_name" in kwargs:
            self.pk_name = kwargs["pk_name"]
        else:
            self.pk_name = "australian_appl_no"


        self.__collection__ = MongoSingleton.get_db()[collection]

        #TODO is PK actually a unique key?
        self.__record__ = self.__collection__.find_one({self.pk_name: patent_application_no})

        #lowercase all keys and remove " chars (IPGOD108)
        if self.__record__ is not None:
            self.__record__ = {key.lower().replace('"', ''): value for key,value in self.__record__.items()}

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
        return self.__record__[self.pk_name.lower()]

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
        if not self.exists() or \
            event_key not in self.__record__ or \
            len(self.__record__[event_key]) is 0:
                return None

        date_str = self.__record__[event_key]
        date = datetime.strptime(date_str.split(' ')[0], "%m/%d/%Y")

        # check for bogus date
        if date.date() == MongoAdapter.DATE_NOT_AVAILABLE.date():
            return None

        return date.date()

    def get_events(self):
        """
        Get the events specified by the record
        :return: list of event dictionaries
        :rtype: list
        """
        pass

    def process_events_list(self, event_dict):
        """
        Using a dict in the format of {"eventname": ("nice name", ["data"]}, build the list of events using the provided
        document
        :param event_document: event document retrieved from mongodb
        :type: dict
        :param event_list:
        :type: dict
        :return: event list
        :rtype: list
        """

        event_list = []

        #retrieve each entry in event_dict
        for event_name, (event_nice, event_data) in event_dict.items():
            date = self.get_event_date(event_name)
            if date is None:
                continue

            # construct the event object and retrieve any data
            event = {
                "date": date,
                "event": event_nice,
                "event_type": event_name,
                "information": [self.__record__[data] for data in event_data if data in self.__record__]
            }

            event_list.append(event)

        return event_list


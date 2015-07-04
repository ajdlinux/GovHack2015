__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

from preprocessing import settings
from pymongo import MongoClient

class MongoSingleton:
    __singleton__ = None

    def __init__(self):
        self.mongo_client = MongoClient(settings.MONGO_IP, settings.MONGO_PORT)

    @staticmethod
    def get():
        """
        Gets the shared MongoClient instance
        :return: mongodb client
        :rtype: MongoClient
        """
        if MongoSingleton.__singleton__ is None:
            MongoSingleton.__singleton__ = MongoSingleton()

        return MongoSingleton.__singleton__.mongo_client

    @staticmethod
    def get_db():
        """
        Gets the configured mongodb database object
        :return: mongodb database
        :rtype: MongoDatabase
        """
        return MongoSingleton.get()[settings.MONGO_DATABASE]
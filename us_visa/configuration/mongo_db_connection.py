import sys
import os
import pymongo
import certifi
from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.constants import DATABASE_NAME, CONNECTION_URL

class MongoDBClient:
    """
    A MongoDB Client for connecting to the database and accessing data.
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("CONNECTION_URL")
                if mongo_db_url is None:
                    raise USvisaException(f"Environment key CONNECTION_URL is not set.", sys)
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=certifi.where())
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys) from e
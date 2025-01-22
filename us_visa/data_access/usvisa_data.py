import sys
import pandas as pd
import numpy as np
from typing import Optional
from us_visa.exception import USvisaException
from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME

class USvisaData:
    """
    Facilitates exporting MongoDB records into a pandas DataFrame.
    """
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys) from e

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            db = self.mongo_client.database if database_name is None else self.mongo_client.client[database_name]
            collection = db[collection_name]
            df = pd.DataFrame(list(collection.find()))
            df.drop(columns=["_id"], errors='ignore', inplace=True)
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e, sys) from e
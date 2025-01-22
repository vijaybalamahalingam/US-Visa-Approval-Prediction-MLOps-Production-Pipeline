import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USvisaData
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        self.data_ingestion_config = data_ingestion_config

    def export_data_into_feature_store(self) -> DataFrame:
        try:
            logging.info("Exporting data from MongoDB")
            usvisa_data = USvisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(self.data_ingestion_config.collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info(f"Data exported to {feature_store_file_path} successfully")
            return dataframe
        except Exception as e:
            raise USvisaException(e, sys) from e

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
        
            training_dir = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(training_dir, exist_ok=True)
        
            testing_dir = os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(testing_dir, exist_ok=True)

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
          
            logging.info(f"Data split into train and test sets and saved to {training_dir} and {testing_dir} respectively.")
        except Exception as e:
            raise USvisaException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe)
            logging.info("Data ingestion process completed successfully.")
            return DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path)
        except Exception as e:
            raise USvisaException(e, sys) from e
import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates data ingestion and returns data ingestion artifacts.
        """
        try:
            logging.info("Starting data ingestion in TrainPipeline")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys) from e

    def run_pipeline(self) -> None:
        """
        Runs the entire training pipeline, handling exceptions and logging progress.
        """
        try:
            logging.info("Running the full training pipeline")
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info("Data ingestion completed successfully")
            # Assuming further steps like data preprocessing, model training, etc., would be handled here.
        except Exception as e:
            raise USvisaException(e, sys) from e
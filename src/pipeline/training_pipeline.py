import os
import sys

from src.logger import logging
from src.exception import DataIngestionError

from src.components.data_ingestion import DataIngestion


try:
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)

except Exception as e:
    logging.error(DataIngestionError('Error occured in data ingestion/pipeline stage'))

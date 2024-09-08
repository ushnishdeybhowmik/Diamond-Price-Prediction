import os
import sys

from src.logger import logging
from src.exception import DataIngestionError

import pandas as pd 
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path  = os.path.join(os.getcwd(), 'artifacts', 'train.csv')
    test_data_path = os.path.join(os.getcwd(),'artifacts', 'test.csv')
    raw_data_path = os.path.join(os.getcwd(),'artifacts', 'raw.csv')


class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        logging.info('Data Ingestion Configuration Done')
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Method Initiated')
        
        try:
            data = pd.read_csv(os.path.join(os.getcwd(), 'notebooks/data', 'gemstone.csv'))
            logging.info('Dataset read as Pandas DataFrame')
            
            data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info('Train test split initiated')
            
            train_set, test_set = train_test_split(data, test_size=0.3, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info('Ingestion of data is completed')
            

            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.error(DataIngestionError('Error occured in data ingestion stage'))
            
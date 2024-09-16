from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import sys
import os

import numpy as np 
import pickle

from src.exception import DataIngestionError, DataTransformationError
from src.logger import logging

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    preprocessor_object_file_path = os.path.join(os.getcwd(), 'artifacts', 'preprocessor.pkl')


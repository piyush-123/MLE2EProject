import os
import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils import get_collection_as_dataframe
from datetime import datetime

FILE_NAME = 'sensor.csv'
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%M%d%Y-%H%M%S')}")
        except Exception as e:
            raise SensorException(e,sys)

class DataIngestionConfig:
    def __init__(self,trainingpipelineconfig:TrainingPipelineConfig):
        try:
            self.database_name = 'learningml'
            self.collection_name = 'sensors'
            self.data_ingestion_dir = os.path.join(trainingpipelineconfig.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception  as e:
            raise SensorException(e,sys)


    def to_dict(self) -> dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)



class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...


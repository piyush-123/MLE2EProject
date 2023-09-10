from sensor.exception import SensorException
from sensor.entity import config_entity
from sensor.components import data_ingestion
import sys


if __name__ == '__main__':
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config)
        data_ingestion = data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
        print(data_ingestion.initiate_data_ingestion())
    except Exception as e:
        raise SensorException(e,sys)



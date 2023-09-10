import pandas as pd
from sensor.logger import logging
from sensor.config import mongo_client
import sys
import os
import yaml
from sensor.exception import SensorException

def get_collection_as_dataframe(database_name:str,collection_name:str):

    try:
        logging.info(f"Reading data from database{database_name} and collection {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns : {df.columns}")
        if "_id" in df.columns:
            logging.info("Dropping column: _id")
            df = df.drop("_id",axis=1)
        logging.info(f"Rows and columns are : {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)


def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,'w') as f:
            yaml.dump(data,f)
    except Exception as e:
        raise SensorException(e,sys)
    
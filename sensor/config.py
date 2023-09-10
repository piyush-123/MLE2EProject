import pymongo
import pandas as pd
import json
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv('MONGO_DB_URL')


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)


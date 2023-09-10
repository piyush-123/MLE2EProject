import pymongo
import pandas as pd
import json
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.environ.get('USER')
PASSWORD=os.environ.get('PASSWORD')
print(USER)
print(PASSWORD)
PATH_NAME = 'aps_failure_training_set1.csv'
DATABASE_NAME = 'learningml'
COLLECTION_NAME = 'sensors'


if __name__ == "__main__":
    df = pd.read_csv(PATH_NAME)
    print(f"The number of rows and columns are : {df.shape}")
    df.reset_index(drop=True,inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())
    connection_string = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority"
    print(connection_string)
    client = pymongo.MongoClient(connection_string)
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)

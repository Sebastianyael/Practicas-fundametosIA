from pymongo import MongoClient

import os
from dotenv import load_dotenv
load_dotenv()

cluster = os.environ.get('MONGO_CLUSTER')
database = os.environ.get('MONGO_DB')
coleccion = os.environ.get('MONGO_COLLECTION')
usuario = os.environ.get('MONGO_USER')
password = os.environ.get('MONGO_PASSWORD')

client = MongoClient(f"mongodb+srv://{usuario}:{password}@{cluster}/{database}") 
db = client[database]
coleccion_uno = db[coleccion] 



coleccion_uno.insert_one({
    "mensaje":"primer registro a la base de datos en la nube sigma 67"
})



import json
 
from pymongo import MongoClient




client = MongoClient('localhost', 27017)

db = client['faith_matthias_diana']

collection_countries = db['countries']


with open('/usr/share/databases/SevenDatabases/code/mongo/countries.json') as f:
  
    file_data = json.load(f)
    

collection_countries.insert(file_data)
    
client.close()
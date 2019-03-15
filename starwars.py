import pymongo
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]

dataUser = {
    "userid": 0,
    "name": 'amb',
    "last_name": "coucou"
}

users = db.users
users.insert_one(dataUser)



db.users.list_indexes() 
import pandas as pd
import requests
peoples = []
i=1
while i < 3:
    r = requests.get('https://swapi.co/api/people/'+ str(i)).json()
    peoples.append(r)
    i = i +1
    
listofClean = []
for elm in peoples:
    clean = {}
    for i in elm:
        if type(elm[i]) is list:
            clean[i] = elm[i][0]
        else:
            clean[i] = elm[i]
    listofClean.append(clean)    
         

            
df = pd.DataFrame.from_dict(listOfClean)
df.head()

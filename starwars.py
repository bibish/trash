#exo Mongo 
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

#exo starwars
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


#exo sqlite
1/ - sqlite3 chinook.db - .tables 2/ .tables '%s' 

3/.schema albums 

4/.fullschema 

5/ select * from tracks; 

6/select * from albums order by ArtistId limit 10; 

7/select Name from tracks order by AlbumId limit 10; 

8/select Name from tracks where AlbumId = 1 limit 10; 

9/select Name from tracks where AlbumId = 1 and Milliseconds > 252980 limit 10 ; 10/select Name,MediaTypeId from tracks where MediaTypeId = 1 or MediaTypeId = 2 order by Name limit 10; select ar.ArtistId,Name, a.AlbumId from artists ar left join albums a on ar. ArtistId = a.ArtistId where ar.ArtistId = a.AlbumId order by AlbumId;

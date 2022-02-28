from mysqlaccessors import connectTo
import pymongo as mg

connectMongo = mg.MongoClient("localhost", 27017)
db = connectMongo['assignment1']
collectionItems = db['items']
cursor = collectionItems.find({})
for document in cursor:
    print(document) 
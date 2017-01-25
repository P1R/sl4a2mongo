#!/usr/bin/env python2.7
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.test
cursor = db.restaurants.find()

for document in cursor:
    print(document)

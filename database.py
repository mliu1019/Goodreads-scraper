import pymongo
import os

def mongoclient():
    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PSWD = os.getenv("MONGODB_PSWD")
    MONGODB_DB   = os.getenv("MONGODB_DB")
    client = pymongo.MongoClient(
        "mongodb+srv://{}:{}@cs242db.crxv1.mongodb.net/{}?retryWrites=true&w=majority".format(MONGODB_USER, MONGODB_PSWD, MONGODB_DB)
    )
    return client.cs242db


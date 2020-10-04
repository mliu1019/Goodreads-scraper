"""Sets up the MongoDB database on the cloud."""
import os
import pymongo


def mongoclient():
    """Function for setting up the database and returns it."""
    mongodb_user = os.getenv("MONGODB_USER")
    mongodb_pswd = os.getenv("MONGODB_PSWD")
    mongodb_db   = os.getenv("MONGODB_DB")
    client = pymongo.MongoClient(
        "mongodb+srv://{}:{}@cs242db.crxv1.mongodb.net/{}?retryWrites=true&w=majority".
        format(mongodb_user, mongodb_pswd, mongodb_db)
    )
    return client.cs242db

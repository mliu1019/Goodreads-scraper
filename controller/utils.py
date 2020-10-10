from database import mongoclient
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

mongo = mongoclient()

def check_book_attribute(attributes):
    numbers = ['rating_count', 'review_count', 'rating']
    for k in numbers:
        if k in attributes:
            attributes[k] = float(attributes[k])
    
    if '_id' in attributes:
        attributes['_id'] = ObjectId(attributes['_id'])
    return attributes

def get_books(attributes):
    return list(mongo.books.find(attributes))

def update_book(attributes, new_attribuets):
    update_one(mongo.books, attributes, new_attribuets)

def create_book(attributes):
    create_one(mongo.books, attributes)

def delete_book(attributes):
    delete_one(mongo.books, attributes)

def create_books(attribute_list):
    create_many(mongo.books, attribute_list)



def delete_one(collection, attributes):
    collection.delete_one(attributes)

def create_many(colleciton, attribute_list):
    colleciton.insert(attribute_list)

def create_one(collection, attributes):
    ret = collection.insert_one(attributes)

def update_one(collection, attributes, new_attribuets):
    if len(new_attribuets) > 0:
        collection.find_one_and_update(attributes, {'$set': new_attribuets})
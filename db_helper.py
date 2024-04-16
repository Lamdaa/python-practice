
import os
from bson import ObjectId
from pymongo import MongoClient


class DBHelper:
    #creating mongo client connection
    collection = None
    
    @classmethod
    def configure_mongo(cls):
        host = os.getenv('MONGO_HOST')
        port = os.getenv('MONGO_PORT')
        database_name = os.getenv('MONGO_DB_NAME')
        collection_name = os.getenv('MONGO_COLLECTION_NAME')
        client = MongoClient(host = host, port = int(port))
        db = client[database_name]
        cls.collection = db[collection_name]
    
    @classmethod
    def get_all_books(cls):
        books = cls.collection.find({})
        return list(books)
    
    @classmethod
    def get_book_by_id(cls,id):
        return cls.collection.find_one({'_id':ObjectId(id)})
    
    @classmethod
    def add_book(cls,book):
        return cls.collection.insert_one(book)
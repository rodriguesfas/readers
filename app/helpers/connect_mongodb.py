"""
    DB Connection
"""

from mongoengine import *
from pymongo import MongoClient
from app.config.database import DB 

class ConnectMongoDB(object):
    
    def __init__(self):
        self.client = MongoClient(DB['hostname'], DB['port'], maxPoolSize=200)
        self.db = self.client[DB['database']]
        self.conn()
        
    def conn(self):
        return self.db
    
    def insert_document_one(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            _id = collection.insert_one(document).inserted_id
            return _id
        except Exception as err:
            return err
        
    def select_document_one(self, collection_name, key):
        try:
            collection = self.db[collection_name]
            result = collection.find_one(key)
            if(result):
                return result
            else:
                return False
        except Exception as err:
            return err
        
    def select_document_all(self, collection_name, key):
        try:
            collection = self.db[collection_name]
            result = collection.find(key)
            
            annotations = []
            
            for anotation in result:
                annotations.append(anotation)

            return annotations
        except Exception as err:
            return err
        
    def update_document_one(self, collection_name, key, document):
        try:
            collection = self.db[collection_name]
            result = collection.update_one(key, document)
            return result
        except Exception as err:
            return err
        
    def delete_document_one(self, collection_name, key):
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(key)
            return result
        except Exception as err:
            return err
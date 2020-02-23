import datetime
from app.database import DB

class Name(object):
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.datetime.utcnow()
 
    def insert(self):
            DB.insertName(collection='names', data=self.json())
 
    def json(self):
        return {
            'name': self.name,
            'created_at': self.created_at
        }
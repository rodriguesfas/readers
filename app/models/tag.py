from app.helpers.connect_mongodb import ConnectMongoDB

class Tag(object):
    
    def __init__(self):
        self.db = ConnectMongoDB()
        
    def save(self, document):
        try:
            db_response = self.db.insert_document('tag', document)
            db_response = {'tag': {'_id': db_response}}
            return db_response
        except Exception as err:
            return "🐞 Saved tag  " + str(err)

    def select_one(self, _id_corpus):
        db_response = self.db.select_document('tag', _id_corpus)
        if db_response:
            return db_response
        else:
            return db_response

    def select_all(self, _id_corpus):
        db_response = self.db.select_document_all_key('tag', _id_corpus)
        if db_response:
            return db_response
        else:
            return db_response

    def update(self, key, document):
        db_response = self.db.update_corpus('tag', key, document)
        if db_response:
            return "tag Successfully Updated!"
        else:
            return "tag Update Error!"

    def delete(self, key):
        _key = {"_id": ObjectId(key)}
        db_response = self.db.delete_corpus('analysis', _key)
        if db_response.deleted_count == 1:
            return {'document': {'delete': True}}
        else:
            return {'document': {'delete': False}}
        
   
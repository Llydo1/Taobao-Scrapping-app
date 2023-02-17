from pymongo import MongoClient

class StoreModel:
    def __init__(self, db_uri, db_name):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db['stores']

# ---------CRUD with ID--------- #

    # Create new store in db_stores
    def create_store(self, store):
        result = self.collection.insert_one(store)
        return str(result.inserted_id)
    
    def get_store_by_id(self, store_id):
        query = {'store_id': store_id}
        return self.collection.find_one(query)
    
    def update_store_by_id(self, store_id, update_data):
        query = {'store_id': store_id}
        update = {'$set': update_data}
        result = self.collection.update_one(query, update)
        return result.modified_count
    
    def delete_store_by_id(self, store_id):
        query = {'store_id': store_id}
        result = self.collection.delete_one(query)
        return result.deleted_count
    
# ---------Other functions--------- #

    
    def get_store_by_name(self, name):
        query = {"name": {"$regex": name, "$options": "i"}}
        stores = self.collection.find(query)
        return [store for store in stores]
    
    
    


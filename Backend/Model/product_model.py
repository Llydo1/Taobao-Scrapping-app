from pymongo import MongoClient

class ProductModel:
    def __init__(self, db_uri, db_name, db_collection_name):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[db_collection_name]

    def get_product_by_id(self, product_id):
        result = self.collection.find_one({'id': product_id})
        return result
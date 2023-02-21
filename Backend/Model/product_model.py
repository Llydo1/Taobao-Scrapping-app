from pymongo import MongoClient

class ProductModel:
    # Init without collection name
    def __init__(self, db_uri, db_name):
        self.__client = MongoClient(db_uri)
        self.__db = self.__client[db_name]

    # Init with collection name
    def __init__(self, db_uri, db_name, collection_name):
        self.__client = MongoClient(db_uri)
        self.__db = self.__client[db_name]
        self.__collection = self.__db[collection_name]

# ---------SETTER--------- #
    def set_collection(self, collection_name):
        self.__collection = self.__db[collection_name]


# ---------CRUD with ID--------- #

    # Create new product in db_products
    def create_product(self, product):
        result = self.__collection.insert_one(product)
        return str(result.inserted_id)
    
    def get_product_by_id(self, product_id):
        query = {"product_id": product_id}
        return self.__collection.find_one(query)
    
    def update_product_by_id(self, product_id, update_data):
        query = {'product_id': product_id}
        update = {'$set': update_data}
        result = self.__collection.update_one(query, update)
        return result.modified_count
    
    def delete_product_by_id(self, product_id):
        query = {'product_id': product_id}
        result = self.__collection.delete_one(query)
        return result.deleted_count
    
# ---------Other functions--------- #
import sys
sys.path.insert(0, '..')
from Model.factory import Factory
from Model.store_model import StoreModel
from Utils.input_manipulate import get_url_input, get_id_input
from Utils.pretty_print import pretty

from Utils.read_write_os import *

class StoreController:
    __store_model: StoreModel  = None

    def __init__(self) -> None:
        self.__store_model = StoreModel("mongodb://localhost:27017/", "store")

    # scrap_store
    # Return item_url_list for productController
    def scrap_store(self) -> str:
        url = get_url_input("Nhập link taobao để cào:")
        store = None

        # Start scraping store
        try:
            store = Factory().create_store(url)
            print("Cào thành công, lưu store vào database...")
        except Exception as e:
            print(e)
            print("Cào thất bại, hãy thử lại")
            return None
        store_id = store.get_store_id()

        # Duplicated checked
        duplicated = self.__store_model.get_store_by_id(store_id)
        if duplicated is not None:
            print("store_id đã tồn tại")
            return store_id, duplicated["item_url_list"]
        
        # Create store to the database
        result = (self.__store_model.create_store(store.get_store()))
        if result is None:
            print("Lưu store thất bại")
            return None
        else:
            print("Lưu store thành công, ID:" +  store.get_store_id())
            return store_id, store.get_item_url_list()

    # get_store_by_id
    def get_store_by_id(self):
        store_id = str(get_id_input("Hãy nhập store_id:"))
        store = self.__store_model.get_store_by_id(store_id)
        if store is None:
            print("store_id không tồn tại")
            return None
        else:
            print("Đã tìm thấy store với ID " + store_id)
            pretty(store)
            return store

    # update_store_by_id
    # it will be quite hard because many things need to update
    

    # delete_store_by_id
    def delete_store_by_id(self):
        store_id = str(get_id_input("Hãy nhập store_id để xóa:"))
        store = self.__store_model.delete_store_by_id(store_id)
        if store is None:
            print("store_id không tồn tại")
            return None
        else:
            print("Xóa thành công store với ID " + store_id)
            return store




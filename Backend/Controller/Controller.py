import sys
sys.path.insert(0, '..')
from Backend.Model.Taobao_World_store import Taobao_World_store
from Backend.Model.Taobao_World_item import Taobao_World_item
import requests
import json
from Utils.read_write_os import *

FOLDER_PATH= "C:\\Users\\beani\\OneDrive\\Desktop\\samsidu\\"

# This class will generate other classes
class __Factory():
    def create_store(self,url,store_name) -> Taobao_World_store:
        store = Taobao_World_store(url, store_name)
        return store

    def create_item(self,url) -> Taobao_World_item:
        item = Taobao_World_item(url)
        return item

class Controller():
    __factory: __Factory

    def __init__(self) -> None:
        self.__factory = __Factory()

    def scrap_store(self,url,store_name) -> bool:
        try:
            store = self.__factory.create_store(url,store_name)
            path = FOLDER_PATH + store_name
            json_path = path + "\\" + store_name +".json"
            create_folder(path)
            write_json_to_file(json_path, store.get_store())
        except Exception as e:
            print(f"An error occurred while scrap Taobao Store: {e}")
            return False
        return True

    def scrap_item(self,url) -> bool:
        try:
            item = self.__factory.create_item(url)
            
        except Exception as e:
            print(f"An error occurred while scrap Taobao item: {e}")
            
        
    def scrap_images(self):
        return True

    def scrap_detail_images(self):
        return True

            



import sys
sys.path.insert(0, '..')
from ..Model.Factory import Factory
from ..Model.product_model import ProductModel
from ..Utils.input_manipulate import get_url_input

import requests
import json
from Utils.read_write_os import *
import pymongo

class StoreController:
    product_model = ProductModel("mongodb://localhost:27017/")

    def scrap_store():
        url = get_url_input("Nhập link taobao để cào:")
        store = Factory.create_store(url)
        print(store)


            



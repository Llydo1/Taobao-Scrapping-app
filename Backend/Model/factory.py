from Model.Taobao_World_store import Taobao_World_store
from Model.Taobao_World_item import Taobao_World_item

class Factory():
    def create_store_from_url_and_name(self,url,store_name) -> Taobao_World_store:
        store = Taobao_World_store(url, store_name)
        return store
        
    def create_store_with_url(self,url) -> Taobao_World_store:
        store = Taobao_World_store(url)
        return store    

    def create_item(self,url, product_id, store_id) -> Taobao_World_item:
        item = Taobao_World_item(url, product_id, store_id)
        return item

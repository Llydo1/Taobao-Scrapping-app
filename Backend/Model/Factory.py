from ..Model.Taobao_World_store import Taobao_World_store
from ..Model.Taobao_World_item import Taobao_World_item

class Factory():
    def create_store(self,url,store_name) -> Taobao_World_store:
        store = Taobao_World_store(url, store_name)
        return store

    def create_item(self,url) -> Taobao_World_item:
        item = Taobao_World_item(url)
        return item

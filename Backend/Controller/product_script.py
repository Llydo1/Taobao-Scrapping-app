from googletrans import Translator
import sys
sys.path.insert(0, '..')

from Controller.store_controller import StoreController
from Controller.product_controller import ProductController

store_id, url_list = StoreController().scrap_store()

ProductController("mongodb://localhost:27017/", "store", str(store_id)).scrap_item_with_url_list_multi_thread(str(store_id),url_list)
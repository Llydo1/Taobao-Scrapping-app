from googletrans import Translator
import sys
sys.path.insert(0, '..')

from Controller.store_controller import StoreController

# store = StoreController().scrap_store()

# store = StoreController().get_store_by_id()

store = StoreController().delete_store_by_id()
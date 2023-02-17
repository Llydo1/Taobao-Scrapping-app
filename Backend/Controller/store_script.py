from googletrans import Translator
import sys
sys.path.insert(0, '..')

from ..Model.Taobao_World_store import Taobao_World_store

store = Taobao_World_store('https://world.taobao.com/dianpu/142967287.htm')

print(store.get_store())
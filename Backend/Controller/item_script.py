from googletrans import Translator
import sys
sys.path.insert(0, '..')

from Taobao.Model.Taobao_World_item import Taobao_World_item_Link

item = Taobao_World_item_Link("https://world.taobao.com/item/644365089158.htm?spm=a21wu.11804641-tw.shop-content.1")

print(item.toJson())
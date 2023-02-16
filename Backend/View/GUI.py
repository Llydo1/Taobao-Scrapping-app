import sys
sys.path.insert(0, '..')
from Taobao.Controller.Controller import Controller

controller = Controller()

controller.scrap_all_item("https://world.taobao.com/dianpu/142967287.htm", "uustudio")
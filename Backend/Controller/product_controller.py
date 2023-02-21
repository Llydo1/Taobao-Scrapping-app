import sys
sys.path.insert(0, '..')
from Model.factory import Factory
from Model.product_model import ProductModel
from Utils.input_manipulate import get_url_input, get_id_input
from queue import Queue
import time


from Utils.read_write_os import *

class ProductController:
    __product_model: ProductModel  = None

    def __init__(self, db_uri, db_name, collection_name) -> None:
        self.__product_model = ProductModel(db_uri, db_name, collection_name)

    def scrap_item_with_url():
        pass

    def scrap_item_with_url_list(self, store_id, url_list):
        url_queue = Queue()
        number_of_product = len(url_list)
        for index, url in enumerate(url_list):
            url = {"url" : url, "index": index}
            url_queue.put(url)

        print("Có tất cả {} sản phẩm để cào".format(number_of_product))
        retries = {}
        success_count = 0
        while not url_queue.empty():
            url_object = url_queue.get()
            index = url_object["index"]
            url = url_object["url"]
            # try:   
            if True:        
                # Do web scraping on url
                # If success, print a tick symbol and increase the successful count
                # If failure, print an x symbol and put the url back in the url
                print("Scraping {}".format(url))
                product_id = store_id + "_" + str(index)
                product = Factory().create_item(url, product_id ,store_id)
                if product is not None:
                    print("✔ Cào thành công sản phẩm {}! Chuẩn bị thêm vào database...".format(url))
                    result = self.__product_model.create_product(product.get_item())
                    if result is not None:
                        success_count+=1
                        print(f"✔ Lưu {success_count}/{number_of_product} sản phẩm thành công, ID:" + product_id)
                    else:
                        print(f"✘ Lưu sản phẩm thất bại....")  
                        if url not in retries:
                            retries[url] = 1
                            url_queue.put(url)
                        else:
                            retries[url] += 1
                            if retries[url] == 3:
                                print(f"Giving up on {url}.")                      
                else:
                    print("✘ Cào thất bại {}. Thử lại sau...".format(url))
                    url_queue.put(url_object)
            # except Exception as e:
            #     print(f"Đã có lỗi xảy ra {url}: {e}")
            #     if url not in retries:
            #         retries[url] = 1
            #         url_queue.put(url)
            #     else:
            #         retries[url] += 1
            #         if retries[url] == 3:
            #             print(f"Giving up on {url}.")
            time.sleep(1) 
        


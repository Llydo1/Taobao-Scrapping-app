import sys
sys.path.insert(0, '..')
from Model.factory import Factory
from Model.product_model import ProductModel
from Utils.input_manipulate import get_url_input, get_id_input
from queue import Queue
import time
import threading


from Utils.read_write_os import *

class ProductController:
    __product_model: ProductModel  = None

    def __init__(self, db_uri, db_name, collection_name) -> None:
        self.__product_model = ProductModel(db_uri, db_name, collection_name)

    def scrap_item_with_url():
        pass

    def scrap_item_with_url_list(self, store_id, url_list):
        url_queue_for_scrapping = Queue()
        number_of_product = len(url_list)
        for index, url in enumerate(url_list):
            url = {"url" : url, "index": index}
            url_queue_for_scrapping.put(url)

        print("Có tất cả {} sản phẩm để cào".format(number_of_product))
        retries = {}
        number_of_scrapping_success = 0
        while not url_queue_for_scrapping.empty():
            url_object = url_queue_for_scrapping.get()
            index = url_object["index"]
            url = url_object["url"]
            try:   
            # if True:        
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
                        number_of_scrapping_success+=1
                        print(f"✔ Lưu {number_of_scrapping_success}/{number_of_product} sản phẩm thành công, ID:" + product_id)
                    else:
                        print(f"✘ Lưu sản phẩm thất bại....")  
                        self.retry_count(url_queue_for_scrapping, retries,url)                    
                     
                else:
                    print("✘ Cào thất bại {}. Thử lại sau...".format(url))
                    self.retry_count(url_queue_for_scrapping, retries,url)                    
            except Exception as e:
                print(f"Đã có lỗi xảy ra {url}: {e}")
                self.retry_count(url_queue_for_scrapping, retries,url)        
            time.sleep(1) 



    def scrap_item_with_url_list_multi_thread(self, store_id, url_list):
        num_threads = 4  # Number of threads to use
        number_of_product = len(url_list)
        url_queue_for_scrapping = Queue()
        for index, url in enumerate(url_list):
            url = {"url" : url, "index": index}
            url_queue_for_scrapping.put(url)
        number_of_scrapping_success = 0
        print("Có tất cả {} sản phẩm để cào".format(number_of_product))

        def worker(url_queue_chunk:Queue): 
            nonlocal number_of_scrapping_success
            retries: dict = {}
            while not url_queue_chunk.empty():
                fail_to_scrap_url = None
                url_object = url_queue_chunk.get()
                index = url_object["index"]
                url = url_object["url"]
                try:
                    save_store_to_db = Factory().create_item(url, store_id + "_" + str(index), store_id)
                    if not save_store_to_db:
                        print("✘ Cào thất bại {}. Thử lại sau...".format(url))
                        fail_to_scrap_url = self.retry_count(url_queue_chunk, retries, url)
                        continue

                    print("Scraping {}".format(url))
                    product_id = store_id + "_" + str(index)
                    product = Factory().create_item(url, product_id ,store_id)
                    print("✔ Cào thành công sản phẩm {}! Chuẩn bị thêm vào database...".format(url))
                    save_product_to_db = self.__product_model.create_product(product.get_item())

                    # Check if product creation is successful
                    if save_product_to_db is None:
                        print(f"✘ Lưu sản phẩm thất bại....")  
                        fail_to_scrap_url = self.retry_count(url_queue_chunk, retries, url)
                        continue

                    number_of_scrapping_success += 1
                    print(f"✔ Lưu {number_of_scrapping_success}/{number_of_product} sản phẩm thành công, ID:" + product_id)

                except Exception as e:
                    print(f"Đã có lỗi xảy ra {url}: {e}")
                    fail_to_scrap_url = self.retry_count(url_queue_chunk, retries, url)

                if fail_to_scrap_url is not None:
                    pass
                time.sleep(1) 
          
        threads = []
        chunk_size = len(url_list) // num_threads
        for i in range(num_threads):
            start = i * chunk_size
            end = (i+1) * chunk_size if i < num_threads-1 else len(url_list)
            url_queue_chunk = Queue()
            for i in range(start, end):
                url_queue_chunk.put(url_queue_for_scrapping.get())
            
            # Remember that Thread argument is a tuple, so it must end with a cp,,a
            thread = threading.Thread(target=worker, args=(url_queue_chunk,))
            threads.append(thread)
            thread.start()
            
        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    def create_product_from_url_and_index(self):
        pass
    
    def retry_count(self, url_queue_for_scrapping:Queue, retries_list:dict, url):
        if url not in retries_list:
            retries_list[url] = 1
            url_queue_for_scrapping.put(url)
        else:
            retries_list[url] += 1
            if retries_list[url] == 3:
                print(f"Giving up on {url}.")
                return url
        return None
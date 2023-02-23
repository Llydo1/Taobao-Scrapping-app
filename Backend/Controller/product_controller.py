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
                        success_count+=1
                        print(f"✔ Lưu {success_count}/{number_of_product} sản phẩm thành công, ID:" + product_id)
                    else:
                        print(f"✘ Lưu sản phẩm thất bại....")  
                        retry_count(url_queue, retries,url)                    
                     
                else:
                    print("✘ Cào thất bại {}. Thử lại sau...".format(url))
                    retry_count(url_queue, retries,url)                    
            except Exception as e:
                print(f"Đã có lỗi xảy ra {url}: {e}")
                retry_count(url_queue, retries,url)        
            time.sleep(1) 



    def scrap_item_with_url_list_multi_thread(self, store_id, url_list):
        num_threads = 4  # Number of threads to use
        number_of_product = len(url_list)
        url_queue = Queue()
        for index, url in enumerate(url_list):
            url = {"url" : url, "index": index}
            url_queue.put(url)
        success_count = 0
        print("Có tất cả {} sản phẩm để cào".format(number_of_product))

        def worker(url_queue_chunk:Queue): 
            nonlocal success_count
            retries: dict = {}
            while not url_queue_chunk.empty():
                url_object = url_queue_chunk.get()
                index = url_object["index"]
                url = url_object["url"]
                try:   
                # if True:        
                    # Do web scraping on url
                    print("Scraping {}".format(url))
                    product_id = store_id + "_" + str(index)
                    product = Factory().create_item(url, product_id ,store_id)
                    if product is not None:
                        print("✔ Cào thành công sản phẩm {}! Chuẩn bị thêm vào database...".format(url))
                        result = self.__product_model.create_product(product.get_item())
                        if result is not None:
                            success_count += 1
                            print(f"✔ Lưu {success_count}/{number_of_product} sản phẩm thành công, ID:" + product_id)
                        
                        # Thất bại
                        else:
                            print(f"✘ Lưu sản phẩm thất bại....")  
                            retry_count(url_queue_chunk, retries,url )                    
                    else:
                        print("✘ Cào thất bại {}. Thử lại sau...".format(url))
                        retry_count(url_queue_chunk, retries,url)                    
                except Exception as e:
                    print(f"Đã có lỗi xảy ra {url}: {e}")
                    retry_count(url_queue_chunk, retries,url )
                time.sleep(1) 

        # Count number of retries for each url

            
        threads = []
        chunk_size = len(url_list) // num_threads
        for i in range(num_threads):
            start = i * chunk_size
            end = (i+1) * chunk_size if i < num_threads-1 else len(url_list)
            url_queue_chunk = Queue()
            for i in range(start, end):
                url_queue_chunk.put(url_queue.get())
            
            # Remember that Thread argument is a tuple, so it must end with a cp,,a
            thread = threading.Thread(target=worker, args=(url_queue_chunk,))
            threads.append(thread)
            thread.start()
            
        # Wait for all threads to finish
        for thread in threads:
            thread.join()


    
def retry_count(url_queue:Queue, retries_list:dict, url ):
    if url not in retries_list:
        retries_list[url] = 1
        url_queue.put(url)
    else:
        retries_list[url] += 1
        if retries_list[url] == 3:
            print(f"Giving up on {url}.")
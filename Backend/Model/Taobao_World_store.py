from .iLink import iLink
from .iStore import iStore
from bs4 import BeautifulSoup
from googletrans import Translator
import re
import requests
import json

class Taobao_World_store(iLink,iStore):
    __url =""
    __soup =""
    __page__number = ""
    __url_list = []
    __total_items = 0
    __item_url_list = []

    def __init__(self, url, store_name=""):
        super(store_name)
        self._store_id = self.__set_store_id_by_url(url)
        self.__url = url
        self.__soup = self._set_soup(url)
        self.__page__number = self.__set_number_of_page()
        self.__url_list = self.__set_url_list(url)
        self.__total_items = self.__set_total_items()
        self.__item_url_list = self.__set_item_url_list()

    def __init__(self, url):
        super(self.__set_store_name_by_souping(url))
        self._store_id = self.__set_store_id_by_url(url)
        self.__url = url
        self.__soup = self._set_soup(url)
        self.__page__number = self.__set_number_of_page()
        self.__url_list = self.__set_url_list(url)
        self.__total_items = self.__set_total_items()
        self.__item_url_list = self.__set_item_url_list()
        
    
# ---------Override function--------- #
    def get_url(self):
        return self.__url

    def get_store_name(self):
        return self.__store_name

    def _set_soup(self, url):
        response = requests.get(url)
        # Parse the page content with BeautifulSoup
        return BeautifulSoup(response.content, "html.parser")

# ---------Setter functions--------- #
    def __set_store_id_by_url(self, url):
        match = re.search(r"dianpu/(\d+)", url)
        if match:
            number = match.group(1)
            return number
        return None
    
    def __set_store_name_by_souping(self, url):
        element = self.__soup.find(class_='info-name')
        return "hehe"

    def __set_url_list(self,url):
        url_list = [url]
        link = url[:-4]
        for i in range(1,self.__page__number):
            url_list.append(link + "_" + str(i+1) + ".htm")
        return url_list

    # set number of page
    def __set_number_of_page(self):
        element = self.__soup.find(class_='pagination-box')
        text = element.find(class_='text-end').text
        number = int(list(filter(str.isdigit, text))[0]) 
        return number
    
    # set number of items
    def __set_total_items(self):
        soup = self._set_soup(self.__url_list[-1])
        block = soup.find(class_="block")
        return len(block.find_all(class_='item')) + 60*(self.__page__number-1)

    # set the list of item
    def __set_item_url_list(self):
        items = []
        # first iterate
        for item in self.__soup.find(class_="block").find_all("a"):
            items.append(item["href"])

        # remaining iterate
        for url in self.__url_list[1:]:
            soup = self.soup(url)
            for item in soup.find(class_="block").find_all("a"):
                items.append(item["href"])   
        return items    

# ---------Getter functions--------- #    
    def get_soup(self):
        return self.__soup
    
    def get_page_number(self):
        return self.__page__number;
    
    def get_url_list(self):
        return self.__url_list

    def get_total_items(self):
        return self.__total_items
    
    def get_item_url_list(self):
        return self.__item_url_list
    
    def get_store(self):
        return {
           "url": self.get_url(),
            "url_list": self.get_url_list(),
            "store_name" : self.get_store_name(),
            "page__number" : self.get_page_number(),
            "total_items" : self.get_total_items(),
            "item_url_list": self.get_item_url_list(), 
        }
    
# ---------Other functions--------- #    
    
    def soup(self,url):
        response = requests.get(url)
        # Parse the page content with BeautifulSoup
        return BeautifulSoup(response.content, "html.parser")

    def toJson(self):
        return json.dumps(self.get_store())
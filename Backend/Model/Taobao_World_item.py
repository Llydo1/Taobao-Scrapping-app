from .iLink import iLink
from .Taobao_World_store import Taobao_World_store
from Utils.https_prefix import add_https_prefix
from bs4 import BeautifulSoup
from selenium import webdriver
from googletrans import Translator
import json


translator = Translator()

class Taobao_World_item(iLink):
    __product_id = ""
    __store_id = ""
    __url =""
    __store: Taobao_World_store = ""
    __soup =""
    __colors: list = []
    __images: list = []
    __detail_images: list = []
    __price = ""
    __current_price = ""
    __detail_information: dict = {}

    # init with store_id
    def __init__(self, url, product_id, store_id, store = None):
        self.__product_id = product_id
        self.__store_id = store_id
        self.__url = url
        self.__store = store
        self.__soup = self._set_soup(url)
        self.__colors = self.__set_colors()
        self.__images = self.__set_images()
        self.__detail_images = self.__set_detail_images()
        self.__current_price = self.__set_current_price()
        self.__price = self.__set_price()
        if(self.__price == "None"):
            self.__price = self.__current_price
        self.__detail_information = self.__set_detail_information()


# ---------Override function--------- #
    def get_product_id(self):
        return self.__product_id
    
    def get_store_id(self):
        return self.__store_id
    
    def get_store_name(self):
        return self.__store.get_store_name()

    def get_url(self):
        return self.__url

    def _set_soup(self, url):
        # Create a webdriver object using the Chrome driver
        driver = webdriver.Chrome()

        # Navigate to a URL
        driver.get(url)

        # Scroll down 500 pixels
        driver.execute_script("window.scrollBy(0, 500);")

        # Get the HTML source of the page after scrolling
        html = driver.page_source

        # Close the webdriver
        driver.quit() 
        return BeautifulSoup(html, 'html.parser')


# ---------Private setter functions--------- #
    def __set_colors(self):
        color_list = []
        sku_right = (self.__soup.find(class_="sku-box")).find(class_="right-content").find_all(class_="property-item")
        for element in sku_right:
            translate_text = translator.translate(element.div.text)
            color_list.append(translate_text.text)
        return color_list

    def __set_images(self):
        images = []
        image_box = self.__soup.find_all(class_="img-box")
        for image in image_box:
            images.append(add_https_prefix(image.img['src'])) 
        return images

    def __set_detail_images(self):
        images = []
        detail_images = self.__soup.find(class_="detail-content").find_all('img')
        for image in detail_images:
            image_url = add_https_prefix(image['src'])
            images.append(image_url) 
        return images

    def __set_price(self):
        return self.__soup.find(class_="private").text
    
    def __set_current_price(self):
        return self.__soup.find(class_="currency").text

    def __set_detail_information(self):
        detail_information = {}
        for li in self.__soup.find(class_="info").find_all('li'):
            translate_text = translator.translate(li.text)
            text1 = translate_text.text
            text1 = text1.split(":")
            detail_information[text1[0]] = text1[1]
        return detail_information


# ---------Getter functions--------- #
    def get_store(self):
        return self.__store
    
    def get_soup(self):
        return self.__soup
    def get_price(self):
        return self.__price

    def get_current_price(self):
        return self.__current_price

    def get_colors(self):
        return self.__colors

    def get_images(self):
        return self.__images

    def get_detail_images(self):
        return self.__detail_images
    
    def get_detail_information(self):
        return self.__detail_information
    
    def get_item(self):
        return {
            "product_id" : self.get_product_id(),
            "store_id": self.get_store_id(),
            "url": self.get_url(),
            "colors" : self.get_colors(),
            "images" : self.get_images(),
            "detail_images" : self.get_detail_images(),
            "price" : self.get_price(),
            "Current price": self.get_current_price(),
            "detail_information" : self.get_detail_information(),
        }

    
# ---------Other functions--------- #   

    def toJson(self):
        return json.dumps(self.get_item())

    

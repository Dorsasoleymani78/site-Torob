from abc import ABC,abstractmethod
import requests
from bs4 import  BeautifulSoup
import json
 
class functions(ABC):
    @abstractmethod
    def Get_topic_url(self):
        pass
    @abstractmethod
    def url_of_page(self):
        pass
    @abstractmethod
    def img_of_page(self):
        pass
    def  get_title(self):
        pass

 #------------------------------------------------------------------------------------------------


   

class get(functions):
    def __init__(self ) -> None:
        self.url="https://harajimanzel.com/shop/"
        self.linkOfPages=[]
        self.urlOfproducts=[]
        self.imgOfProducts=[]
        self.PriceOfProducts=[]
        self.titleOfProducts=[]
        self.get_all_products()
     
    def __str__(self) -> str:
        return  self.linkOfPages,self.urlOfproducts,self.PriceOfProducts,self.titleOfProducts

    def Get_topic_url(self):
        res= requests.get(self.url)
        Topic_url=BeautifulSoup(res.content,"html.parser")
        for i in range(1,17):
            self.linkOfPages.append(self.url+"page/"+str(i)+'/')
         
    def url_of_page(self):
        for url in self. linkOfPages:
            res= requests.get(url)
            products=BeautifulSoup(res.content,"html.parser")
            nlink=products.find('ul',class_='products columns-4')
            n=nlink.findAll('a',{'class':'woocommerce-LoopProduct-link woocommerce-loop-product__link'})
            for item in n:
               self.urlOfproducts.append(item['href'] )
      
    def img_of_page(self):
          for url in self. linkOfPages:
            res= requests.get(url)
            products=BeautifulSoup(res.content,"html.parser")
            nlink=products.find('ul',class_='products columns-4')
            img=nlink.findAll('img',{'class':'attachment-woocommerce_thumbnail size-woocommerce_thumbnail'})
            for item in img:
              self.imgOfProducts.append(item['src'] )
           
          
             
    def get_price(self):
        for url in self.linkOfPages:
            res= requests.get(url)
            products=BeautifulSoup(res.content,"html.parser")
            price=products.findAll('bdi')
            for item in price:
             
                self.PriceOfProducts.append(item.text)
                    
           
       
            
    def get_title(self):
        for url in self.linkOfPages:
            res= requests.get(url)
            products=BeautifulSoup(res.content,"html.parser")
            title=products.findAll('h2',class_='woocommerce-loop-product__title')
            for item in title:
              self.titleOfProducts.append((item.text).lower() )
         
 
    def get_all_products(self):
        def fun1():
            self.Get_topic_url()
            self.url_of_page()
            self.img_of_page()
            self.get_title()
            self.get_price()
        fun1()

 
 
 
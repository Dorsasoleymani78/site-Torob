from abc import ABC,abstractmethod
import requests
from bs4 import  BeautifulSoup
from DAL import select_from_shopping
from model import product
#https://moblomiz.com/Products/classic-sofa
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
    def __init__(self) -> None:
        self.url="https://moblomiz.com/Products/#"
        
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
       nlink=Topic_url.select('div.suppa_column>a')
   
       for l in nlink:
           self.linkOfPages.append(l['href'])
           
    def url_of_page(self):
        for url in self. linkOfPages:
            res= requests.get("https://moblomiz.com"+url)
            products=BeautifulSoup(res.content,"html.parser")
            nlink=products.find('ul',class_='products products-b')
            n=nlink.findAll('a',{'class':'link-to-product'})
            for item in n:
               self.urlOfproducts.append(item['href'] )
      
    def img_of_page(self):
        for url in self.linkOfPages:
            res= requests.get("https://moblomiz.com"+url)
            products=BeautifulSoup(res.content,"html.parser")
            nlink=products.find('ul',class_='products products-b')
            img=nlink.findAll('img')
            for item in img:
              self.imgOfProducts.append(item['src']  )
          
             
    def get_price(self):
        for url in self.linkOfPages:
            res= requests.get("https://moblomiz.com"+url)
            products=BeautifulSoup(res.content,"html.parser")
            nlink=products.find('ul',class_='products products-b')
            price=nlink.findAll('span',{'class':'woocommerce-Price-amount amount'})
            for item in price:
                     self.PriceOfProducts.append(item.text)
          
           
       
            
    def get_title(self):
        for url in self.linkOfPages:
            res= requests.get("https://moblomiz.com"+url)
            products=BeautifulSoup(res.content,"html.parser")
            nlink=products.find('ul',class_='products products-b')
            img=nlink.findAll('img')
          
            for item in img:
           
              self.titleOfProducts.append(item['alt'].lower() )

    def get_all_products(self):
            def fun1():
                self.Get_topic_url()
                self.url_of_page()
                self.img_of_page()
                self.get_title()
                self.get_price()
            fun1()
 

 
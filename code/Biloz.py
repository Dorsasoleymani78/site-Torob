from abc import ABC,abstractmethod
import requests
from bs4 import  BeautifulSoup
 
 
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
        self.url='https://bizlo.ir/'
        self.linkOfPages=[]
        self.urlOfproducts=[]
        self.imgOfProducts=[]
        self.PriceOfProducts=[]
        self.titleOfProducts=[]
        self.get_all_products()

    
    def Get_topic_url(self):
        res= requests.get(self.url)
        Topic_url=BeautifulSoup(res.content,"html.parser")
        link=Topic_url.select('div.menuContainer>div.nav-column>ul>li>a')
        for i in link:
            self.linkOfPages.append(i['href'])
        

    def url_of_page(self):
        for url in self. linkOfPages:
            for u in range(65):
                res= requests.get(url+"index.php?page="+str(u))
                products=BeautifulSoup(res.content,"html.parser")
                link=products.select('div.col-sm-10.col-md-6.col-lg-4>div.auction-item-2>div.auction-thumb>a')
                for item in link:
                    self.urlOfproducts.append(item['href'] )
                
               
      
    def img_of_page(self):
            for url in self. linkOfPages:
                for u in range(65):
                    res= requests.get(url+"index.php?page="+str(u))
                    products=BeautifulSoup(res.content,"html.parser")
                    link=products.select('div.col-sm-10.col-md-6.col-lg-4>div.auction-item-2>div.auction-thumb>a>img')
                    for item in link:
                          self.imgOfProducts.append(item['src'] )
           
          
             
    def get_price(self):
        for url in self.linkOfPages:
                for u in range(65 ):
                    res= requests.get(url+"index.php?page="+str(u))
                    products=BeautifulSoup(res.content,"html.parser")
                    price=products.select('div.col-sm-10.col-md-6.col-lg-4>div.auction-item-2>div.auction-content>div.bid-area>div.bid-amount.text-center>div.amount-content>div.amount')
                    for item in price:
                          self.PriceOfProducts.append(item.text )
                    
           
       
            
    def get_title(self):
        for url in self.linkOfPages:
                for u in range(65):
                    res= requests.get(url+"index.php?page="+str(u))
                    products=BeautifulSoup(res.content,"html.parser")
                    title=products.select('div.col-sm-10.col-md-6.col-lg-4>div.auction-item-2>div.auction-content>h6.title.text-center>a')
                    for item in title:
                         self.titleOfProducts.append(item.text)
    

    def get_all_products(self):
        def fun1():
            self.Get_topic_url()
            self.url_of_page()
            self.img_of_page()
            self.get_title()
            self.get_price()
        fun1()

# get1=get()
# get1.Get_topic_url()
# for i in get1.linkOftopic:
#     print(i)

 
# get1.url_of_page()
# for i in get1.linkOfPages:
#     print(i)
# print(len(get1.linkOfPages))
# get1.url_of_product()
# for i in get1.urlOfproducts:
#     print(i)
# print(len(get1.urlOfproducts))
# get1.img_of_page()
# for i in get1.imgOfProducts:
#     print(i)
# print(len(get1.imgOfProducts))
# get1.get_title()
# for i in get1.titleOfProducts:
#     print(i)
# print(len(get1.titleOfProducts))
 
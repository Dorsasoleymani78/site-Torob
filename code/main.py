from model import product
from DAL import Insertproduct,select_from_shopping
#--------------------------------------------------------------
def Insert_to_T_shop(madul):  
      m=madul.get()
      len1=len(m.urlOfproducts)
      for i in range(len1):
        product1=product(str(m.titleOfProducts[i]),str(m.urlOfproducts[i]),str(m.imgOfProducts[i]),str(m.PriceOfProducts[i]))
        if  "تومان" in product1.price:
           Insertproduct(product1)
#----------------------------------------------------------------------------------------------------------------
def Insert_Madule():
    madule=select_from_shopping()
    for item in madule:
       Insert_to_T_shop(item)

 
 
 
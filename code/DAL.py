from model import product,shopping, temp_shopping, user
from dbConnection import dbConnect
import importlib
db=dbConnect()
Mycursor=db.cursor()
      
def select_from_shopping():
    list1=[]
    Mycursor.execute('select * from t_shop')
    x=Mycursor.fetchall()
    for seller in x :
        if seller[5]=="active":
            print(seller[4])
            madule=importlib.import_module(seller[4]) 
            list1.append(madule) 
    return list1
#----------------------------------------------------------------------------------------
 
def Insertproduct(product):
    try:
       var=(product.url,product.img,product.title,product.price)
       query="Insert INTO t_product(url,img,title,price)values(%s,%s,%s,%s)"
       Mycursor.execute(query,var)
       db.commit()
       return True
    except:
        return False
#-------------------------------------------------------------------
def insert_to_search():
    try:
        query="select title from t_product"
        Mycursor.execute(query)
        res=Mycursor.fetchall()
        db.commit()
        return [str(item) for item in res ]
    except:
        return False
#--------------------------------------------------------------------
def searchProduct(title):
    try:
        query=f"select * from t_product  where title={title}"
        Mycursor.execute(query)
        res=Mycursor.fetchall()
        db.commit()
        for item in res:
            product1=product(item[0],item[1],item[2],item[3])
        return product1  
    except:
        return False       
#-------------------------------------------------------------------------------
def delete():
    try:
        query="delete from T_product"
        Mycursor.execute(query)
        db.commit()
        return True
    except:
        return False
#-----------------------------------------------------------------------------
def searchForUsers(userName,password):
    user1=None
    query=f"Select * from t_user where userName='{userName}'and password='{password}'"
    Mycursor.execute(query)
    res=Mycursor.fetchall()
    for item in res:
        user1=user(item[0],item[1],item[2],item[3],item[4],item[5])
    return user1
#------------------------------------------------------------------------------
def Findshopping(shoName):
    query=f"select * from temp_shop where name='{shoName}'"
    Mycursor.execute(query)
    res=Mycursor.fetchall()
    for item in res:
       temp_shopping1= temp_shopping(item[0],item[1],item[2])
    return  temp_shopping1
#-------------------------------------------------------------------
def Insert_to_tempShopping(temp_shopping):
    try:
       var=(temp_shopping.name,temp_shopping.ActivityBasining,temp_shopping.link)
       query="Insert INTO temp_shop(name,ActivityBasin,link)values(%s,%s,%s)"
       Mycursor.execute(query,var)
       db.commit()
       return True
    except:
        return False
#---------------------------------------------------------------------
def Apply(shopping):
    try:
        var=(shopping.Id,shopping.name,shopping.ActivityBasin,shopping.MaduleName,shopping.link,shopping.Conditions)
        query="Insert INTO t_shop(Id,name,ActivityBasin,MaduleName,link,Conditions)values(%s,%s,%s,%s,%s,%s)"
        Mycursor.execute(query,var)
        db.commit()
        return True
    except:
        return False
#--------------------------------------------------------------------------------------------------
def delete_from_temp_shop(name):
    try:
        query=f"delete  from temp_shop where name='{name}'"
        Mycursor.execute(query)
        db.commit()
        return True
    except:
        return False

#----------------------------------------------------------------------------------------------------
def search_from_t_shop(name):
    try:
        query=f"select * from t_shop where name='{name}'"
        Mycursor.execute(query)
        res=Mycursor.fetchall()
        for item in res:
            shopping1=shopping(item[0],item[1],item[2],item[3],item[4],item[5])
        return shopping1
    except:
        return False
#-----------------------------------------------------------------------------------------------------
def update_t_shop(text,name):
    try:
        query=f"update t_shop set Conditions='{text}' where name='{name}'"
        Mycursor.execute(query)
        db.commit()
        return True
    except:
        return False
#--------------------------------------------------------------------------------------------------------
def Insert_to_t_user(user):
    try:
        var=(user.name,user.family,user.userName,user.password,user.role_Id)
        query="Insert INTO t_user(name,family,userName,password,role_Id)values(%s,%s,%s,%s,%s)"
        Mycursor.execute(query,var)
        db.commit()
        return True
    
    except:
        return False

#---------------------------------------------------------------------------------
def show_list_of_shopps():
    try:
        query="select name,link from t_shop"
        Mycursor.execute(query)
        res=Mycursor.fetchall()       
        return dict(res)
    except:
        return False
#---------------------------------------------------------------------------------
def sabt_password(username,password):
    try:
        query=f"select userName from t_user where userName='{username}'"
        Mycursor.execute(query)
        res=Mycursor.fetchall()
        if res==[]:
           return False
        else:
            query1=f"update t_user set password='{password}' where userName='{username}'"
            Mycursor.execute(query1)
            db.commit()
            return True
    except:
        return False


 
 
 
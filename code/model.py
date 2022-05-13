class shopping:
    def __init__(self,Id,name,ActivityBasin,link,MaduleName,Conditions) :
        self.Id=Id
        self.name=name 
        self.ActivityBasin=ActivityBasin
        self.link=link 
        self.MaduleName=MaduleName
        
        self.Conditions=Conditions

    def __str__(self) -> str:
         return f"Id:{self.Id}\t Name:{self.name}\t ActivityBasining:{self.ActivityBasin}\tlink:{self.link}\tmaduleName:{self.MaduleName}\t codition is{self.Conditions}"
#=============================================================================================================       
class temp_shopping:
    def __init__(self,name,ActivityBasining,link) -> None:
        self.name=name
        self.ActivityBasining=ActivityBasining
        self.link=link

    def __str__(self) -> str:
         return f"name:{self.name}\t ActivityBasining:{self.ActivityBasining}\t link:{self.link}"
      
#================================================================================================================== 
class userRegister :
    def __init__(self ,name,family,userName,password,role_Id) -> None:
       
        self.name=name
        self.family=family
        self.userName=userName
        self.password=password
        self.role_Id=role_Id
         
    def __str__(self) -> str:
        return f"name:{self.name}userName:{self.userName}\t password:{self.password} "
#=========================================================================================================================
class user :
    def __init__(self,userId,name,family,userName,password,role_Id) -> None:
        self.userId=userId
        self.name=name
        self.family=family
        self.userName=userName
        self.password=password
        self.role_Id=role_Id
         
    def __str__(self) -> str:
        return f"name:{self.name}userName:{self.userName}\t password:{self.password} "
#=============================================================================================================
class product:
    def __init__(self,title,url,img,price) :
        self.title=title
        self.url=url
        self.img=img
        self.price=price

    
    def __str__(self) -> str:
         return f"title :{self.title}\t url:{self.url}\t img:{self.img}\t  price:{self. price} "

#============================================================================================================================
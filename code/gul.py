from tkinter import *
from tkinter import messagebox
import tkinter
import DAL
from ttkwidgets.autocomplete import AutocompleteCombobox
from model import  shopping, temp_shopping, userRegister 
import main
import re
import importlib

class gui:
    def createForm(self,f,width,height):
        w=width
        h=height
        ws=f.winfo_screenwidth()
        hs=f.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        f.geometry("%dx%d+%d+%d"%(w,h,x,y))
#--------------------------------------------------------------    
    def por_kardan_List(self,objectList):
        for item in DAL.insert_to_search():
            i=item.split(',')
            j=''.join(i[0])
            n=j.split('(')
            objectList.append(''.join(n[1]))
        return objectList
#-------------------------------------------------------------------
    def khali_kardan_list(self,objectList):
        objectList.clear()
        return objectList
        
#-------------------------------------------------------------------
    def __init__(self):
      
        self.root=Tk()
        self.objectList=[]
        self.por_kardan_List(self.objectList)
        self.createForm(self.root,600,300)
        frame=tkinter.Frame(self.root,bg='darkturquoise')
        frame.pack(expand=True)
   
        tkinter.Label(master=frame,text='چه میخواهید؟',bg='darkturquoise',font = ('Times',21)).pack()
        entry = AutocompleteCombobox(master=frame, width=30,font=('Times', 18),
        completevalues=sorted(self.objectList,key=lambda str:str.lower()))
        entry.pack()
 
        btnSearch=tkinter.Button(master= self.root,text="جستجو",font = ('Times',18),bg='darkcyan')
        btnSearch.bind("<Button>",lambda event:self.show_Products(event,entry.get()))
        btnSearch.pack(expand=True, side=LEFT)

        btnEnter=tkinter.Button(master= self.root,text="ورود",font =('Times',18),bg='darkcyan')
        btnEnter.bind('<Button>',self.Enter)
        btnEnter.pack(expand=True,side=LEFT)

        btnshop=tkinter.Button(master= self.root,text="لیست فروشگاه",font =('Times',18),bg='darkcyan')
        btnshop.bind('<Button>',self.showShopps)
        btnshop.pack(expand=True,side=LEFT)
 


        self.root.mainloop()
    #------------------------------------------------------------------------------------------------
    shoppspanel=None
    def showShopps(self,event):
        global shoppspanel
        shoppspanel=Toplevel(self.root)
        self.createForm(shoppspanel,300,150)
        frame1=tkinter.LabelFrame(master=shoppspanel,text="لیست فروشگاه ها",fg='darkcyan',font =('Times',13),width=300,height=250)
        frame1.grid(row=0,column=1,padx=8,pady=8)
        shoppsName=DAL.show_list_of_shopps()
        row=0
        for key,value  in shoppsName.items():
              column=0
              tkinter.Label(master=frame1,text=key).grid(row=row,column=column)
              column+=1
              tkinter.Label(master=frame1,text=value).grid(row=row,column=column)
              row+=1

        shoppspanel.mainloop()

    #---------------------------------------------------------------------------------------------------
    productpanel=None
    def show_Products(self,event,title):
        global productpanel
        productpanel=Toplevel(self.root)
        product1=DAL.searchProduct(title)
        self.createForm(productpanel,1200,1000)
       
        Frame1=tkinter.LabelFrame(master=productpanel ,width=1000,height=900,text="اطلاعات محصول",bg='paleturquoise'  )
        Frame1.pack(expand=True,padx=50,pady=10)
       
        labeltitle1=Label(master=Frame1,text=" نام محصول" )
        labeltitle1.grid(row=0,column=0,padx=50,pady=10)
        labeltitle2=Label(master=Frame1,text=product1.title )
        labeltitle2.grid(row=0,column=1,columnspan=2,padx=50,pady=10)

        labelurl1=Label(master=Frame1,text="لینک صفحه" )
        labelurl1.grid(row=1,column=0,padx=50,pady=10)
        labelurl2=Label(master=Frame1,text=product1.url )
        labelurl2.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

        Labelimg1=Label(master=Frame1,text="عکس محصول" )
        Labelimg1.grid(row=2,column=0,padx=50,pady=10)
        Labelimg2=tkinter.Label(master=Frame1,text=product1.img )
        Labelimg2.grid(row=2,column=1,columnspan=2,padx=50,pady=10)

        Labelprice1=Label(master=Frame1,text="قیمت محصول" )
        Labelprice1.grid(row=3,column=0,padx=50,pady=10)
        Labelprice2=Label(master=Frame1,text=product1.price )
        Labelprice2.grid(row=3,column=1,columnspan=2,padx=50,pady=10)
        productpanel.lift()
    #--------------------------------------------------------------------------------
    vurudPanel=None
    def Enter(self,event):
        global vurudPanel
        vurudPanel=Toplevel(self.root)
        self.createForm(vurudPanel,400,200)
        Label1=Label(master=vurudPanel,text="نام کاربری",font = ('Times',13))
        Label1.grid(row=0,column=0,pady=10,padx=10)

        entry1=tkinter.Entry(master=vurudPanel,bg='darkturquoise',font = ('Times',13))
        entry1.grid(row=0,column=2,padx=8,pady=10 )

        Label2=Label(master=vurudPanel,text="رمز عبور",font = ('Times',13))
        Label2.grid(row=1,column=0,pady=10,padx=10)

        entry2=tkinter.Entry(master=vurudPanel,bg='darkturquoise',show='*',font = ('Times',13))
        entry2.grid(row=1,column=2,padx=8) 

        def ischecked():
            entry2.config(show=var.get())

        var=StringVar(vurudPanel)
        check1=tkinter.Checkbutton(master=vurudPanel,text="نمایش دادن" ,variable=var ,onvalue=entry2.get(),offvalue='*',command=ischecked)
        check1.grid(row=2,column=2,padx=8)
        
        
        frame1=tkinter.LabelFrame(master=vurudPanel)
        frame1.grid(row=4,column=0,columnspan=3,padx=10,pady=10)
 
        button1=tkinter.Button(master=frame1,text="ورود",bg='darkcyan',font = ('Times',13))
        button1.grid(row=0,column=0 , padx=20,pady=4)  
        button1.bind("<Button>",lambda event:self.Login(event,entry1.get(),entry2.get()))

        btnRegister=tkinter.Button(master=frame1,text="ثبت نام",font = ('Times',13),bg='darkcyan' )
        btnRegister.bind('<Button>',self.Register)
        btnRegister.grid(row=0,column=1,padx=25 ) 

        btnRegister=tkinter.Button(master=frame1,text="بازیابی رمز عبور",font = ('Times',13),bg='darkcyan' )
        btnRegister.bind('<Button>',self.reset)
        btnRegister.grid(row=0,column=2,padx=25 ) 
        vurudPanel.lift()
    #-----------------------------------------------------------------------------------
    def reset(self,event):
     
        result=messagebox.askquestion("Form","آیا می خواهید رمز عبور خود را بازیابی کنید؟")
        if result=='yes':
            self.Calc_reset()
        else:
            pass

    #--------------------------------------------------------------------------------------------------

    FormResetPassword=None
    def Calc_reset(self):
        global FormResetPassword
        FormResetPassword=Toplevel(vurudPanel)
        self.createForm(FormResetPassword,350,250)
        frame1=tkinter.LabelFrame(master=FormResetPassword,text="ورود اطلاعات",font = ('Times',10) )
        frame1.grid(row=0,column=0,pady=10,padx=10)

        labeluserName=Label(master=frame1,text="نام کاربری",font = ('Times',13))
        labeluserName.grid(row=2,column=0,pady=10,padx=10)
        EnteruserName=tkinter.Entry(master=frame1,bg='darkturquoise',font = ('Times',13))
        EnteruserName.grid(row=2,column=1,pady=10,padx=10)
         
        labelpassword1=Label(master=frame1,text="رمزعبور",font = ('Times',13))
        labelpassword1.grid(row=3,column=0,pady=10,padx=10)
        Enterpassword1=tkinter.Entry(master=frame1,bg='darkturquoise',font = ('Times',13))
        Enterpassword1.grid(row=3,column=1,pady=10,padx=10)

        labelpassword2=Label(master=frame1,text=" تکرار رمز عبور",font = ('Times',13))
        labelpassword2.grid(row=4,column=0,pady=10,padx=10)
        Enterpassword2=tkinter.Entry(master=frame1,bg='darkturquoise',font = ('Times',13))
        Enterpassword2.grid(row=4,column=1,pady=10,padx=10)
   
        
        frame2=tkinter.LabelFrame(master=FormResetPassword,text="",font = ('Times',10) )
        frame2.grid(row=5,column=0,columnspan=2,pady=10,padx=10)
            
        buttonfinish=Button(master=FormResetPassword,text="ثبت",bg='darkcyan',font = ('Times',18))
        buttonfinish.grid(row=5,column=0,columnspan=2)
        buttonfinish.bind("<Button>",lambda event:self.sabt_Password_reseted(event,EnteruserName.get(),Enterpassword1.get(),Enterpassword2.get()))
       
        FormResetPassword.mainloop()
    #-----------------------------------------------------------------------------------------
    def sabt_Password_reseted(self,event,username,password,repetpassword):
        if re.search(r'.{5,30}',password):
            if password==repetpassword :
                res=DAL.sabt_password(username,password)
                if res==True :
                    messagebox.showinfo("اطلاع","عملیات با موفقیت انجام شد")
                else:
                 messagebox.showerror("خطا","عملیات با موفقیت انجام نشد")

            else:
                 messagebox.showerror("خطا","داده های فیلد رمز عبور و تکرار رمز عبور باهم مغایرت دارد")
        else:
            messagebox.showerror("خطا","رمز عبور مناسب وارد کنید")

    #--------------------------------------------------------------------------------------
    FormRegister=None
    def Register(self,event):
        global FormRegister
        FormRegister=Toplevel(self.root)
        self.createForm(FormRegister,600,300)

        frame1=tkinter.LabelFrame(master=FormRegister,text="ورود اطلاعات",font = ('Times',10) )
        frame1.grid(row=0,column=0,pady=10,padx=10)

        labelName=tkinter.Label(master=frame1,text="نام",font = ('Times',10))
        labelName.grid(row=0,column=0,pady=10,padx=10)
        EnterName=tkinter.Entry(master=frame1,bg='darkturquoise')
        EnterName.grid(row=0,column=1,pady=10,padx=10)

        labelFamily=Label(master=frame1,text="نام نام خانوادگی",font = ('Times',10))
        labelFamily.grid(row=1,column=0,pady=10,padx=10)
        EnterFamily=tkinter.Entry(master=frame1,bg='darkturquoise')
        EnterFamily.grid(row=1,column=1,pady=10,padx=10)

        labeluserName=Label(master=frame1,text="نام کاربری",font = ('Times',10))
        labeluserName.grid(row=2,column=0,pady=10,padx=10)
        EnteruserName=tkinter.Entry(master=frame1,bg='darkturquoise',font = ('Times',10))
        EnteruserName.grid(row=2,column=1,pady=10,padx=10)
          

        labelpassword=Label(master=frame1,text="رمزعبور",font = ('Times',10))
        labelpassword.grid(row=3,column=0,pady=10,padx=10)
        Enterpassword=tkinter.Entry(master=frame1,bg='darkturquoise')
        Enterpassword.grid(row=3,column=1,pady=10,padx=10)

        Frame2=LabelFrame(master=FormRegister,text="هویت")
        Frame2.grid(row=1,column=0,pady=5,padx=5)
        
        l=StringVar(Frame2)
        licenses={"مدیر":"1","مشتری":"2"}
        i=0
        for item,value in licenses.items():
               Radiobutton(master=Frame2,text=item,variable=l,value=value ).grid(row=0,column=i,pady=10,padx=10)
               i+=1
        
        buttonRegister=tkinter.Button(master=FormRegister,text="ثبت نام",bg='darkcyan')
        buttonRegister.bind("<Button>",lambda event:self.The_operation_of_Register(event,EnterName.get(),EnterFamily.get(),EnteruserName.get(),Enterpassword.get(),l.get()))
        buttonRegister.grid(row=2,column=0,columnspan=2)
 
        FormResetPassword.mainloop()
        
    #-----------------------------------------------------------------------------------------------------------    
    def The_operation_of_Register(self,event,name,family,userName,password,role_Id):
  
         
        pattern=r'[A-Z|a-z]{3,}'
        name1= "" if re.search(pattern,name)  else messagebox.showerror("خطا","نام   مناسب وارد کنید")
       
        family1="" if re.search(pattern,family) else messagebox.showerror("خطا","نام خانوادگی مناسب وارد کنید")
            
        username1="" if re.search(r'^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',userName)else messagebox.showerror("خطا","نام کاربری مناسب وارد کنید")
      
        pass1=""if re.search(r'.{5,30}',password)else messagebox.showerror("خطا","رمز عبور مناسب وارد کنید")
             
        

        if   re.search(pattern,name)and re.search(pattern,family)and re.search(r'^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',userName)and re.search(r'.{5,30}',password):
            user1=userRegister (name,family,userName,password,role_Id)
            res=DAL.Insert_to_t_user(user1)


        if res==True and re.search(pattern,name)and re.search(pattern,family)and re.search(r'^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',userName)and re.search(r'.{5,30}',password):
               messagebox.showinfo('اطلاع','عملیات با موفقیت انجام شد')
        else:
              messagebox.showerror('خطا','عملیات با موفقیت انجام نشد')

    #-----------------------------------------------------------------------------------
    customerplane=None
    Adminplane=None
 
    def Login(self,event,userName,password):
        user1=DAL.searchForUsers(userName,password)
        if user1 is not None:
            if user1.role_Id==1:
                global Adminplane
                Adminplane=Toplevel(self.root)
                self.createForm(Adminplane,600,200)
                labelName=tkinter.Label(master=Adminplane,text="نام فروشگاه",font = ('Times',15))
                labelName.grid(row=0,column=0,pady=10,padx=10)
                EntryName=tkinter.Entry(master=Adminplane,bg='darkturquoise',font = ('Times',15))
                EntryName.grid(row=0,column=1,padx=10,pady=10)
                Frame2=tkinter.LabelFrame(master= Adminplane )
                Frame2.grid(row=1,column=0,pady=10,padx=10,columnspan=2)

                buttonCheck=tkinter.Button(master=Frame2,text="چک کردن",bg='darkcyan',font = ('Times',13))
                buttonCheck.grid(row=2,column=0,columnspan=2)
                buttonCheck.bind('<Button>',lambda event:self.check_shopping(event,EntryName.get()))
                 
                buttonLicense=tkinter.Button(master=Frame2,text="تغییر مجوز",bg='darkcyan',font = ('Times',13))
                buttonLicense.grid(row=2,column=3,columnspan=2)
                buttonLicense.bind('<Button>',lambda event:self.change_License(event,EntryName.get()))
                Adminplane.lift()

            elif user1.role_Id==2:
                global customerplane
                
                customerplane=Toplevel(self.root)
                self.createForm(customerplane,400,250)
                Frame1=tkinter.LabelFrame(master= customerplane,text="ثبت اطلاعات" )
                Frame1.grid(row=0,column=4,pady=10,padx=10,columnspan=2)
               
                labelName1=tkinter.Label(master=Frame1,text="نام فروشگاه",font = ('Times',15))
                labelName1.grid(row=0,column=4,padx=10,pady=10)
                EntryName2=tkinter.Entry(master=Frame1,bg='darkturquoise',font = ('Times',15))
                EntryName2.grid(row=0,column=5,padx=10,pady=10)

                labelActive1=tkinter.Label(master=Frame1,text="حوضه فعالیت",font = ('Times',15) )
                labelActive1.grid(row=1,column=4,padx=10,pady=10)
                EntryActive2=tkinter.Entry(master=Frame1,bg='darkturquoise',font = ('Times',15) )
                EntryActive2.grid(row=1,column=5,padx=10,pady=10)

                labellink1=tkinter.Label(master=Frame1,text="آدرس فروشگاه",font = ('Times',15) )
                labellink1.grid(row=2,column=4,padx=10,pady=10)
                Entrylink2=tkinter.Entry(master=Frame1,bg='darkturquoise',font = ('Times',15) )
                Entrylink2.grid(row=2,column=5,padx=10,pady=10)
               
                btn_sabt=tkinter.Button(master=customerplane,text="ثبت فروشگاه",bg='darkcyan',font = ('Times',15))
                btn_sabt.grid(row=6,column=4,columnspan=2)
                btn_sabt.bind('<Button>',lambda event:self.sabt(event,EntryName2.get(),EntryActive2.get(),Entrylink2.get()))
                customerplane.lift()
        else:

            messagebox.showerror('خطا','نام کاربری یا رمز عبور شما نادرست است')
    #--------------------------------------------------------------------------------------
    def sabt(self,event,name,ActivityBasin,link):
        pattern=r'[A-Z|a-z]{3,}'
        name1= "" if re.search(pattern,name)  else messagebox.showerror("خطا","نام   مناسب وارد کنید")

        ActivityBasin1= "" if re.search(pattern,ActivityBasin)  else messagebox.showerror("خطا","نام   مناسب وارد کنید")

        patternLink='(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
       
        link1= "" if re.search(patternLink,link)  else messagebox.showerror("خطا","آدرس  مناسب وارد کنید")
       
        if re.search(pattern,name) and re.search(pattern,ActivityBasin) and re.search(patternLink,link) :
            temp_shopping2=temp_shopping(name,ActivityBasin,link)
            res=DAL.Insert_to_tempShopping(temp_shopping2)

        if res==True and re.search(pattern,name)and re.search(pattern,ActivityBasin) and re.search(patternLink,link):
               messagebox.showinfo('اطلاع','عملیات با موفقیت انجام شد')
        else:
    
              messagebox.showerror('خطا','عملیات با موفقیت انجام نشد')
    #-----------------------------------------------------------------------------------
    FormTayid=None
    def check_shopping(self,event,name):
        global FormTayid 
        FormTayid =Toplevel(self.root)
        self.createForm(FormTayid,500,400)
        shopping1=DAL.Findshopping(name)
        frame1=tkinter.LabelFrame(master=FormTayid,text="اطلاعات فروشگاه",fg='darkcyan',font = ('Times',15) )
        frame1.grid(row=0,column=2,padx=5,pady=5)
 
        labelName1=tkinter.Label(master=frame1,text="نام فروشگاه",font = ('Times',13))
        labelName1.grid(row=0,column=4,padx=10,pady=10)
        labelName2=tkinter.Label(master=frame1,text=shopping1.name,font = ('Times',13))
        labelName2.grid(row=0,column=5,padx=10,pady=10)

        labelActive1=tkinter.Label(master=frame1,text="حوضه فعالیت",font = ('Times',13))
        labelActive1.grid(row=2,column=4,padx=10,pady=10)
        labelActive2=tkinter.Label(master=frame1,text=shopping1.ActivityBasining,font = ('Times',13))
        labelActive2.grid(row=2,column=5,padx=10,pady=10)

        
        labellink1=tkinter.Label(master=frame1,text="آدرس فروشگاه",font = ('Times',13))
        labellink1.grid(row=3,column=4,padx=10,pady=10)
        labellink2=tkinter.Label(master=frame1,bg='darkturquoise',text=shopping1.link,font = ('Times',13))
        labellink2.grid(row=3,column=5,padx=10,pady=10)

        labelCode1=tkinter.Label(master=frame1,text="کد",font = ('Times',13))
        labelCode1.grid(row=4,column=4,padx=10,pady=10)
        Entrycode2=tkinter.Entry(master=frame1,bg='darkturquoise',font = ('Times',13) )
        Entrycode2.grid(row=4,column=5,padx=10,pady=10)

        labelMadule1=tkinter.Label(master=frame1,text="نام ماژول",font = ('Times',13))
        labelMadule1.grid(row=5,column=4,padx=10,pady=10)
        EntryMadule2=tkinter.Entry(master=frame1,bg='darkturquoise',font = ('Times',13))
        EntryMadule2.grid(row=5,column=5,padx=10,pady=10)

        labelcondition1=tkinter.Label(master=frame1,text="شرایط",font = ('Times',13) )
        labelcondition1.grid(row=6,column=4,padx=10,pady=10)
        labelcondition2=tkinter.Label(master=frame1,text="",bg='darkturquoise',font = ('Times',13) )
        labelcondition2.grid(row=6,column=5,padx=10,pady=10)

 

        Frame2=tkinter.LabelFrame(master=FormTayid,text="شرایط",fg='darkcyan')
        Frame2.grid(row=1,column=2 )

        def clicked():
            labelcondition2.config(text=l.get())
        
        l=StringVar(Frame2)
        licenses={"active":"active","disactive":"disactive"}
        i=0
        for item,value in licenses.items():
               Radiobutton(master=Frame2,text=item,variable=l,value=value,command=clicked,selectcolor='darkcyan').grid(row=0,column=i)
               i+=1
        
        def check():
            if labelcondition2.cget("text")=='active':
                madule=importlib.import_module(EntryMadule2.get())
                main.Insert_to_T_shop(madule)
             
                self.por_kardan_List(self.objectList)
        
        frame3=tkinter.LabelFrame(master=FormTayid ,fg='darkcyan')
        frame3.grid(row=2,column=2 )
        buttonApply=tkinter.Button(master=frame3,text="اجازه دادن",bg='darkcyan',font = ('Times',13))
        buttonApply.grid(row=1,column=4,columnspan=2)
        buttonApply.bind('<Button>',lambda event:[self.Apply(event,Entrycode2.get(),labelName2.cget("text"),labelActive2.cget("text"),labellink2.cget("text"),EntryMadule2.get(),labelcondition2.cget("text")),check])

        buttonDisApply=tkinter.Button(master=frame3,text="اجازه ندادن",bg='darkcyan',font = ('Times',13))
        buttonDisApply.grid(row=1,column=6,columnspan=2)
        buttonDisApply.bind('<Button>',lambda event:self.DisApply(event,labelName2.cget("text")))
 
        FormTayid.lift()
    #--------------------------------------------------------------
    def Apply(self,event,Id,name,ActivityBasining,link,MaduleName,Condition):

        Id1="" if re.search(r'\d{1,}',Id) else messagebox.showerror('خطا','کد معتبر وارد کنید')
    
        MaduleName1="" if re.search(r'[A-Z a-z]{3,}',MaduleName) else messagebox.showerror('خطا','نام ماژول معتبر وارد کنید')
        
        if re.search(r'\d{1,}',Id)  and re.search(r'[A-Z a-z]{3,}',MaduleName):
            shpopping1=shopping(Id,name,ActivityBasining,link,MaduleName,Condition)
            res=DAL.Apply(shpopping1)
            DAL.delete_from_temp_shop(name)

        if res==True and re.search(r'\d{1,}',Id) and re.search(r'[A-Z a-z]{3,}',MaduleName):
               messagebox.showinfo('اطلاع','عملیات با موفقیت انجام شد')
        else:
              messagebox.showerror('خطا','عملیات با موفقیت انجام نشد')
    #---------------------------------------------------------------------------
    def DisApply(self,event,name):
        res=DAL.delete_from_temp_shop(name)
        if res==True:
               messagebox.showinfo('اطلاع','عملیات با موفقیت انجام شد')
        else:
              messagebox.showerror('خطا','عملیات با موفقیت انجام نشد')
    #------------------------------------------------------------------------------
    FormLicense=None
    def change_License(self,event,name):
        global FormLicense
        FormLicense=Toplevel(self.Adminplane)
        self.createForm(FormLicense,500,350)
        shopping1=DAL.search_from_t_shop(name)
        frame1=tkinter.LabelFrame(master=FormLicense,text="اطلاعات فروشگاه",fg='darkcyan' )
        frame1.grid(row=0,column=0,padx=5,pady=5)


        labelCode1=Label(master=frame1,text="کد") 
        labelCode1.grid(row=0,column=4,padx=10,pady=10)
        labelcode2=Label(master=frame1,text=shopping1.Id) 
        labelcode2.grid(row=0,column=5,padx=10,pady=10)

        labelName1=Label(master=frame1,text="نام فروشگاه") 
        labelName1.grid(row=1,column=4,padx=10,pady=10)
        labelName2=Label(master=frame1,text=shopping1.name) 
        labelName2.grid(row=1,column=5,padx=10,pady=10)

        labelActive1=Label(master=frame1,text="حوضه فعالیت" )
        labelActive1.grid(row=2,column=4,padx=10,pady=10)
        labelActive2=Label(master=frame1,text=shopping1.ActivityBasin) 
        labelActive2.grid(row=2,column=5,padx=10,pady=10)

        labellink1=tkinter.Label(master=frame1,text="آدرس فروشگاه",font = ('Times',13))
        labellink1.grid(row=3,column=4,padx=10,pady=10)
        Entrylink2=tkinter.Label(master=frame1,text=shopping1.link,font = ('Times',13))
        Entrylink2.grid(row=3,column=5,padx=10,pady=10)

        labelMadule1=Label(master=frame1,text="نام ماژول" )
        labelMadule1.grid(row=4,column=4,padx=10,pady=10)
        labelMadule2=Label(master=frame1,text=shopping1.MaduleName) 
        labelMadule2.grid(row=4,column=5,padx=10,pady=10)

        labelcondition1=Label(master=frame1,text="شرایط" ) 
        labelcondition1.grid(row=5,column=4,padx=10,pady=10)
        labelcondition2=Label(master=frame1,text=shopping1.Conditions ) 
        labelcondition2.grid(row=5,column=5,padx=10,pady=10)
        
        Frame2=tkinter.LabelFrame(master=FormLicense,text="تغییر دادن",fg='darkcyan')
        Frame2.grid(row=1,column=0 )
        
        l=StringVar(Frame2)
        licenses={"active":"active","disactive":"disactive"}
        i=0
        for item,value in licenses.items():
               Radiobutton(master=Frame2,text=item,variable=l,value=value ).grid(row=0,column=i)
               i+=1
        
        def clicked(event):
            labelcondition2.config(text=l.get()) 

        def check(event):
            if labelcondition2.cget("text")=='active':
                madule=importlib.import_module(labelMadule2.cget("text"))
                main.Insert_to_T_shop(madule)
                self.por_kardan_List(self.objectList)
            else:
                self.khali_kardan_list(self.objectList)
                DAL.delete()
                main.Insert_Madule()
                self.por_kardan_List(self.objectList)
 
        

        buttonChangeLicense=tkinter.Button(master=FormLicense,text=" تغییر دادن",bg='darkcyan')
        buttonChangeLicense.grid(row=2,column=0,columnspan=2,padx=5,pady=5)       
        buttonChangeLicense.bind('<Button>',lambda event:[self.change_condition(event,l.get(),labelName2.cget("text")),clicked(event),check(event)])
    
        FormLicense.lift() 
    #-----------------------------------------------------------------------
    def change_condition(self,event,condition,name):
            res=DAL.update_t_shop(condition,name)
            if res==True:
                messagebox.showinfo('اطلاع','عملیات با موفقیت انجام شد')
            else:
                messagebox.showerror('خطا','عملیات با موفقیت انجام نشد')

 
 
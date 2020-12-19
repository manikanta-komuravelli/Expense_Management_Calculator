# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:53:44 2020

@author: manik
"""
# To be used as an expense managment tool

from tkinter import * 
import New_Registration
import Login_Details


top = Tk()  
  
top.title('Expense_Managment')  

top.geometry("400x200")

usernamelist=[]
passwordlist=[]
emaillist=[]

def registration():    
    def save():
        x= username.get()
        y= password.get()
        z= email.get()
        
        usernamelist.append(x)
        passwordlist.append(y)
        emaillist.append(z)
        New_Registration.save(usernamelist,passwordlist,emaillist)
        reg.destroy()
        
# call the registration module to enter the new registration credentials    
    reg= Toplevel(top)
    reg.title('New_Registration')
    username= StringVar()
    password= StringVar()
    email= StringVar()
    
    Label(reg,text='ENTER USERNAME:').grid(row=1,column=1)
    Entry(reg, textvariable=username).grid(row=1,column=2)
    Label(reg,text='ENTER PASSWORD:').grid(row=2,column=1)
    Entry(reg, textvariable=password, show='*').grid(row=2,column=2)
    Label(reg,text='ENTER EMAIL-ID').grid(row=3,column=1)
    Entry(reg, textvariable=email).grid(row=3,column=2)

    
    Button(reg, text="OK", command=save).grid(row=4,column=2)
    
    reg.mainloop()



def Login():
    print(top)
    def details():
        login_username_list=[]
        login_password_list=[]
        forgot_email_list=[]    
        x= login_username.get()
        y= login_password.get()
        print (x)
        login_username_list.append(x)
        login_password_list.append(y)
        Login_Details.user_info(login_username_list,login_password_list,top,login)
        login.destroy()
        
        
        
    login= Toplevel(top)
    login.title('Login') 
    login_username= StringVar()
    login_password= StringVar()
    
    Label(login,text='ENTER USERNAME:').grid(row=1,column=1)
    Entry(login, textvariable=login_username).grid(row=1,column=2)
    Label(login, text='OR').grid(row=1,column=3)
    Label(login,text='Enter EMAIL:').grid(row=1,column=4)
    Entry(login, textvariable=email_username).grid(row=1,column=5)
    Label(login,text='ENTER PASSWORD:').grid(row=2,column=1)
    Entry(login, textvariable=login_password, show='*').grid(row=2,column=2)
    
    Button(login, text="OK", command=details).grid(row=4,column=2)
    
    
        
count=0     
Button(top,text='New Registration',command=registration).place(relx=0.3,rely=0.3, width=100)

Button(top,text='User Login',command=Login).place(relx=0.3,rely=0.5, width=80)

top.mainloop()



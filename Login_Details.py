# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:13:13 2020

@author: manik
"""
import os
import pandas as pd
from tkinter import *
import Expense_Details

# login_username_list=['manu']
# login_password_list=['1hayabusa']

def user_info(login_username_list,login_password_list,top,login):
    
    mypath= os.path.join(os.getenv('programdata'), 'expense_managment')
    file_name= 'registration.csv'
    success= bool
    status= 'User not Found'
    print ("19",login_username_list[0])
    if os.path.isfile(os.path.join(mypath,file_name)):
        filepath= os.path.join(mypath,file_name)
        reg_file= pd.read_csv(filepath)
        for j in range(len(reg_file)):
            if login_username_list[0] == reg_file.loc[j,'Username']:
                status= 'User Found'
                break
            
        for j in range(len(reg_file)):
            if login_username_list[0] == reg_file.loc[j,'Username'] and status== 'User Found':
                if login_password_list[0] == reg_file.loc[j,'Password']:
                    success= True
                else:
                    success= False
    else:
        messagebox.showinfo("Info", "No Registration done yet",)
                
    if success== True:
        print ('User Found')
        login.destroy()
        print ("Line NO:40",login_username_list[0])
        Expense_Details.savedetails(top,login_username_list[0])
        
        
    elif success== False:
        print('Wrong Password')
        user_info= Toplevel(top)
        messagebox.showinfo("Info", "Wrong Password",)
        user_info.destroy()
        
    if status== 'User not Found':
        print ('User not found')
        messagebox.showinfo("Info", "User not found, Please Register",)
        
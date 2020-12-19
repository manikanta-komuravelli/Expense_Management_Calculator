# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:52:16 2020

@author: manik
"""

from tkinter import *
import pandas as pd
import os
import Expense_Details

def save_details(datelist,grocerylist,utilitylist,rentlist,misclist,others,otherslist,expense,login_username_list):
    
    datelist= datelist
    grocerylist=grocerylist
    utilitylist=utilitylist
    rentlist=rentlist
    misclist=misclist
    otherslist=otherslist
    others=others[0]
    df2=pd.DataFrame
    if others != '':
        df2=pd.DataFrame({'Date':datelist,
                          'Groceries':grocerylist,
                          'Utility':utilitylist,
                          'Rent':rentlist,
                          'Misc':misclist,
                          others:otherslist
                          })
    else:
        df2=pd.DataFrame({'Date':datelist,
                          'Groceries':grocerylist,
                          'Utility':utilitylist,
                          'Rent':rentlist,
                          'Misc':misclist
                          })
        
    required_columns=['Date','Groceries','Utility','Rent','Misc']
    required_columns.append(others)
    
    
    mypath= os.path.join(os.getenv('programdata'), 'expense_managment')
    file_name= login_username_list+'expensedetails.csv'
    
    if os.path.isdir(mypath):
        if os.path.isfile(os.path.join(mypath,file_name)): 
            filepath= os.path.join(mypath,file_name)
            expense_files= pd.read_csv(filepath)
            df3= expense_files.append(df2, ignore_index=True)
            df3.reset_index()
            #print (df3)
            df3.to_csv(filepath,index=False)
            messagebox.showinfo("Info", "Expenses Copied",)
            
     
        else:
            expense_files= pd.DataFrame({'Date':['x'],
                  'Groceries':['x'],
                  'Utility':['x'],
                  'Rent':['x'],
                  'Misc':['x']
                  })
            filepath= os.path.join(mypath,file_name)
            df3= expense_files.append(df2, ignore_index=True)
            df3.reset_index()
            df3.to_csv(filepath,index=False)
            messagebox.showinfo("Info", "Expenses Copied",)
    
    else:
        os.mkdir(mypath)
        expense_files= pd.DataFrame({'Date':['x'],
              'Groceries':['x'],
              'Utility':['x'],
              'Rent':['x'],
              'Misc':['x']
              })
        filepath= os.path.join(mypath,file_name)
        df3= expense_files.append(df2, ignore_index=True)
        df3.reset_index()
        df3.to_csv(filepath,index=False)
        messagebox.showinfo("Info", "Expenses Copied",)
        
        


# datelist= ['17/08/2020']
# grocerylist=['']
# utilitylist=['']
# rentlist=['']
# misclist=['115']
# otherslist=['700']
# others=['newexpense']
        
        
# save_details(datelist,grocerylist,utilitylist,rentlist,misclist,others,otherslist)        

        
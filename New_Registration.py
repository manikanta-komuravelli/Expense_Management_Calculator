# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:20:17 2020

@author: manik
"""

import os
import pandas as pd

def save(usernamelist,passwordlist,emaillist):
    # creating a dataframe to fetch the values entered from the user
    df2=pd.DataFrame({'Username':usernamelist,
                      'Password':passwordlist,
                      'Email':emaillist
                      })
    
    required_columns=['Username','Password','Email']
    
    # Creating a directory to store the registration data
    mypath= os.path.join(os.getenv('programdata'), 'expense_managment')
    file_name= 'registration.csv'
    
    #Checking if the expense management directory exists or not.
    if os.path.isdir(mypath):
        #checking if the registration file exists or not, if exists appends the file with the new registration
        #details
        if os.path.isfile(os.path.join(mypath,file_name)): 
            filepath= os.path.join(mypath,file_name)
            reg_file= pd.read_csv(filepath)
            df3= reg_file.append(df2, ignore_index=True)
            df3.reset_index()
            df3[required_columns].to_csv(filepath)
        # creating the registration file if the expense management folder exists and appends the file with registration details  
        else:
            reg_file= pd.DataFrame({'Username':['x'],
                  'Password':['x'],
                  'Email':['x']
                  })
            filepath= os.path.join(mypath,file_name)
            df3= reg_file.append(df2, ignore_index=True)
            df3.reset_index()
            df3[required_columns].to_csv(filepath)
    # creating the expense management folder and registration file for the first time     
    else:
        os.mkdir(mypath)
        reg_file= pd.DataFrame({'Username':['x'],
              'Password':['x'],
              'Email':['x']
              })
        filepath= os.path.join(mypath,file_name)
        df3= reg_file.append(df2, ignore_index=True)
        df3.reset_index()
        df3[required_columns].to_csv(filepath)
    
# usernamelist=['manu','minnu']
# passwordlist=['hayabusa','hayabusa']
# emaillist=['manikanta461@gmail.com','ragaspoorthy@gmail.com']


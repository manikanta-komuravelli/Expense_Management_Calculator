# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:22:12 2020

@author: manik
"""



from tkinter import *
import pandas as pd
import os
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def showexpenses(startdate,enddate,username,expense,view):


    mypath= os.path.join(os.getenv('programdata'), 'expense_managment')
    file_name= username+'expensedetails.csv'
    filepath= os.path.join(mypath,file_name)
    
    df= pd.read_csv(filepath)
    df= df.fillna(0)
    print (df)
    
    cols= list(df.columns)
    print (cols)
    df_final=pd.DataFrame(columns=cols)
    
    cols.remove('Date')
    
    date1= startdate
    date2= enddate
    
    date1_strip= time.strptime(date1,"%d/%m/%Y")
    date2_strip= time.strptime(date2,"%d/%m/%Y")
    
    date_list=[]
    for i in range(len(df)):
        try:
            dataframe_date= time.strptime(df.loc[i,'Date'],"%d-%m-%Y")
            if dataframe_date >= date1_strip and dataframe_date <= date2_strip:
                date_list.append(df.loc[i,'Date'])
        except:
            continue
    
    date_list=list(set(date_list))
    date_list.sort()
    
    
    newdf= df.groupby('Date')
    print(newdf)
    k=0
    
    for date_ in date_list:
        df3= newdf.get_group(date_)
        for i in cols:
            df3[i]=df3[i].astype('float')
        value = df3[cols].sum(axis=0)
        #print(date_)
        #print (value)    
        df_final= df_final.append(value,ignore_index=True)
        df_final.loc[k,'Date']= date_
        k+=1
    
    #print(df_final)    
    df_final.loc[:,'Total']=df_final[cols].sum(axis=1)
    #print(df_final)  
    
    df_final= df_final.loc[:,(df_final!=0).any(axis=0)]
    cols= list(df_final.columns)
    final_cols_list= list(df_final.columns)
    final_cols_list.remove('Date')
    final_cols_list.remove('Total')
    
    df_pie=df_final
    df_pie= df_pie.set_index('Date')
    #print(df_pie)
    df_pie= df_pie.transpose()
    #print (df_pie)
    df_pie= df_pie.drop('Total')
    
    root1= Toplevel(expense)
    figure1 = plt.Figure(figsize=(16,9))
    ax1 = figure1.add_subplot()
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack()
    
    df_pie.plot(kind='pie',subplots=True, startangle=90, shadow=True, legend = False, 
                    autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
                      figsize=(16,9),ax=ax1)
    
    df_pie2=df_final
    df_pie2= df_pie2.set_index('Date')
    #print(df_pie2)
    
    root2= Toplevel(expense)    
    figure2 = plt.Figure(figsize=(16,9))
    ax2 = figure2.add_subplot()
    bar2 = FigureCanvasTkAgg(figure2, root2)
    bar2.get_tk_widget().pack()
        
    df_pie2.plot(kind='pie',subplots=True, startangle=90, shadow=True, legend = False, 
                    autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
                      figsize=(16,9),ax=ax2)
    
    df_final.loc['Total',:]= df_final[cols].sum(axis=0)
    df_final.loc['Total','Date']= 'Total'
        

    root3 = Toplevel(expense)
    print("linenumber:",root3)         
        
    celltext=[]
    for row in range(len(df_final)):
        celltext.append(df_final.iloc[row])
    figlen= len(df_final.columns)+4
    figwid= int(len(df_final.columns))/2
    figure3= plt.figure(figsize=(figlen,figwid))
    ax3 = figure3.add_subplot()    
    ax3.table(cellText=celltext, colLabels=df_final.columns, loc='center')
    bar3 = FigureCanvasTkAgg(figure3, root3)
    bar3.get_tk_widget().pack() 
    
    df_final=df_final.drop(['Total'])
    
    
    root4= Toplevel(expense)
    
    totaltext=[]
    for row in range(len(df_final)):
        totaltext.append(df_final.loc[row,['Date','Total']])
    
    fig2wid= (int(len(df_final))*1)
    figure4= plt.figure(figsize=(6,fig2wid))
    ax4 = figure4.add_subplot()    
    ax4.table(cellText=totaltext, colLabels=['Date','Total'], loc='center')
    bar4 = FigureCanvasTkAgg(figure4, root4)
    bar4.get_tk_widget().pack()
    
    
    
    # x_offset= -0.03
    # y_offset= 0.02
    #print(df_final)
    root5= Toplevel(expense)
    figure5 = plt.Figure(figsize=(16,9))
    ax5 = figure5.add_subplot()
    bar5 = FigureCanvasTkAgg(figure5, root5)
    bar5.get_tk_widget().pack()
    
    df_final.plot(kind='bar',x='Date',y='Total',logy=True,ax=ax5)
    for p in ax5.patches:
        b=p.get_bbox()
        val = format(b.y1 + b.y0)        
        ax5.annotate(val, ((b.x0 + b.x1)/2, b.y1))    
        


# startdate= '01/08/2020'
# enddate='03/08/2020'
# username='manu'
# showexpenses(startdate,enddate,username)
    
        
        
        
        
        
        

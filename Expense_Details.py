# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:54:01 2020

@author: manik
"""


from tkinter import *
import Save_Expense_Details
import View_Expense_Details

def clear_contents(date,grocery,utility,rent,misc,savings,othersentry,otherslistentry):
    date.set('')
    grocery.set('')
    rent.set('')
    misc.set('')
    savings.set('')
    othersentry.set('')
    otherslistentry.set('')


    

def savedetails(top,login_username_list):
    expense= Toplevel(top)
    expense.title('Expense Details')
    
    
    def View_Expense():
        
        def submit_view_expense():  
            viewdate1list=[]
            viewdate2list=[]
            viewdate1list.append(viewdate1.get())
            viewdate2list.append(viewdate2.get())
            
            startdate=str(viewdate1list[0])
            enddate=str(viewdate2list[0])
            
            print(startdate,enddate,username)
            View_Expense_Details.showexpenses(startdate,enddate,username,expense,view)
            viewdate1.set('')
            viewdate2.set('')
            view.destroy()
            
        print ("Inside View Expense")
        view= Toplevel(expense)
        view.title('View Expenses')
        
        viewdate1= StringVar()
        viewdate2= StringVar()
        username= login_username_list
        
        
        Label(view,text="Enter Start Date(dd/mm/yyyy)").grid(row=1,column=0)
        Entry(view,textvariable=viewdate1).grid(row=1,column=1)
        Label(view,text="Enter End Date(dd/mm/yyyy)").grid(row=2,column=0)
        Entry(view,textvariable=viewdate2).grid(row=2,column=1)
        Button(view,text="Submit",command=submit_view_expense).grid(row=3,column=1)
        
        view.mainloop()
        
        
        
    
        
    def Save_Expense():
        datelist= []
        grocerylist=[]
        utilitylist=[]
        rentlist=[]
        misclist=[]
        others=[]
        otherslist=[]
        datelist.append(date.get())
        grocerylist.append(grocery.get())
        utilitylist.append(utility.get())
        rentlist.append(rent.get())
        misclist.append(misc.get())
        others.append(othersentry.get())
        otherslist.append(otherslistentry.get())
        
        Save_Expense_Details.save_details(datelist,grocerylist,utilitylist,rentlist,misclist,others,otherslist,expense,login_username_list)
        clear_contents(date,grocery,utility,rent,misc,savings,othersentry,otherslistentry)
 
        
    date=StringVar()
    grocery=StringVar()
    utility=StringVar()
    rent=StringVar()
    misc=StringVar()
    savings=StringVar()
    othersentry=StringVar()
    otherslistentry=StringVar()
    
    
    
    Label(expense,text="Date(dd/mm/yyyy)").grid(row=1,column=0)
    Entry(expense,textvariable=date).grid(row=1,column=1)
    print ("linenumber: 60", date)
    Label(expense,text="Groceries").grid(row=2,column=0)
    Entry(expense,textvariable=grocery).grid(row=2,column=1)
    Label(expense,text="Utilities").grid(row=3,column=0)
    Entry(expense,textvariable=utility).grid(row=3,column=1)
    Label(expense,text="Rent").grid(row=4,column=0)
    Entry(expense,textvariable=rent).grid(row=4,column=1)
    Label(expense,text="Misc").grid(row=5,column=0)
    Entry(expense,textvariable=misc).grid(row=5,column=1)
    Label(expense,text="Savings").grid(row=6,column=0)
    Entry(expense,textvariable=savings).grid(row=6,column=1)
    Label(expense,text="Enter your own expense name and value below", wraplength=300).grid(row=7,column=0)
    Entry(expense,textvariable=othersentry).grid(row=8,column=0)
    Entry(expense,textvariable=otherslistentry).grid(row=8,column=1)
    Button(expense,text="View Expenses",command=View_Expense).grid(row=9,column=1)
    Button(expense,text="Save Enteries",command= Save_Expense).grid(row=9,column=0)
    
    
    expense.mainloop()

#savedetails()
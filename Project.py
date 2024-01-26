import os
import datetime     
from tabulate import tabulate

table=[]
No_of_Expenses=int(input("Enter the number of Expenses = "))

def expense():  
    Total_expense=0
    while True:
        try:
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime.date(year=year, month=month, day=day)
            break
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
    while True:
            try:
                Expense=int(input("Enter the Expense ammount = "))
                break
            except ValueError:
                 print("Invalid input. Please enter a valid input.")
                 Expense=int(input("Enter the Expense ammount = "))

    Expense_category=input("Enter the Expense category = ")
    Paid=input("The Ammmount Was Paid To = ")
    Payment_Method=input("Enter the Payment Method = ")
    Total_expense=Total_expense+Expense

    list_of_details=[i+1,date,Paid,Payment_Method,Expense_category,Expense,Total_expense]
    table.append(list_of_details)



for i in range(No_of_Expenses):
    print("Enter the Date of Payment")
    expense()

header=["SL.No","Date of payment","Paid to","Payement method","Expense Category","Expense Amount","Total Expense"]

with open("Expense.txt","a") as f:
        f.write(tabulate(table,headers=header,tablefmt="grid"))
with open("Expense.txt","r") as f:
    r=f.read()
    print(r)

if os.path.exists("Expense.txt"):
    print("File exist")
else:
     print("File not exist")

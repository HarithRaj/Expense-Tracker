import os
import datetime     
from tabulate import tabulate

table=[]

No_of_Expenses=int(input("Enter the number of Expenses = "))
Total_expense=0


for i in range(No_of_Expenses):
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
    Paid=input("Paid TO = ")
    Payment_Method=input("Payment Method = ")
    Total_expense=Total_expense+Expense

    list_of_details=[i+1,date,Paid,Payment_Method,Expense_category,Expense,Total_expense]
    table.append(list_of_details)
    
header=["SL.No","Date of payment","Paid to","Payement method","Expense Category","Expense Amount","Total Expense"]

with open("Expense.txt","a") as f:
        f.write(tabulate(table,headers=header,tablefmt="grid"))
with open("Expense.txt","r") as f:
    r=f.read()
    print(r)
exit()

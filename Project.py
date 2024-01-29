import os
import datetime
import time     
from tabulate import tabulate

table=[]

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

def func():
    input('PRESS ENTER KEY TO VIEW OBJECTIVES')
    print("OBJECTIVE")
    print()
    print("The objective of an expense tracker is to help individuals or organizations effectively manage their finances by keeping track of their expenses. Here are some specific objectives and benefits:")
    print()
    print("1.Financial Awareness: An expense tracker allows users to understand where their money is going. By categorizing expenses, users can identify areas where they are \n overspending and make necessary adjustments to their budget.")
    print()
    print("2.Budgeting: Expense trackers help users set and stick to a budget by providing insights into their spending habits. Users can allocate funds to different categories and track their progress towards staying within budget limits.")
    print()
    print("3.Identifying Trends: With historical expense data, users can identify spending trends over time. This information can be valuable for making informed financial\n decisions and planning for the future.")
    print()
    print("4.Financial Goal Setting: Expense trackers can help users set financial goals and track their progress towards achieving them. Whether it's saving for a vacation, \n paying off debt, or building an emergency fund, users can monitor their financial goals and adjust their spending habits accordingly.")
    print()
    print("5.Tax Preparation: Keeping track of expenses throughout the year can simplify the process of filing taxes. Users can easily access detailed records of their\n expenditures, making it easier to claim deductions and maximize tax savings.")
    print()
    print("6.Financial Accountability: For businesses or organizations, expense trackers promote financial accountability among employees by requiring them to document and \n justify their expenses. This helps prevent misuse of funds and ensures that expenditures align with organizational objectives.")
    print()
    print("Overall, the objective of an expense tracker is to empower individuals and organizations to make informed financial decisions, optimize their spending habits, \nand achieve their financial goals.")
    print()
    input('PRESS ENTER START EXPENSE TRACKER')
func()
print()
time.sleep(2)

No_of_Expenses=int(input("Enter the number of Expenses = "))
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

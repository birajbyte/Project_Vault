

import datetime
class Expense:

    def __init__(self, id , name , amount , expense_type , date = None):
        self.expense_id = id
        self.name = name
        self.amount = float(amount)
        self.expense_type = expense_type

        if date is None:
            self.date = datetime.date.today().strftime("%Y-%m-%d")
        else:
            self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.expense_id = 1
    
    def add_expense(self):
        name = input("Enter the description of expense")
        amount = input("Enter the expense amount: ").strip()
        expense_type = input("Enter the expense type: ").lower()
        date = input("Enter Date of expense:")
        new_expense = Expense(self.expense_id , name , amount , expense_type , date)
        self.expenses.append(new_expense)
        self.expense_id += 1

        print(f"Successfully added: '{name}' (${amount}) to {expense_type}")


    def view_expense(self):
        if not self.expenses:
            print("Expenses are not added yet!")
            return
        for expense in self.expenses:
            print(f"Expense_id:{expense.expense_id}|Name:{expense.name}|Expense_type:{expense.expense_type}|Spent_Amount:{expense.amount}|Date:{expense.date}")

    


        
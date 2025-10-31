class Expense:
    def __init__(self, expense_id, description, amount):
        self.id = expense_id
        self.description = description
        self.amount = amount


class ExpenseModel:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, description, amount):
        expense = Expense(self.next_id, description, amount)
        self.expenses.append(expense)
        self.next_id += 1

    def delete_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_all_expenses(self):
        return self.expenses

    def get_total(self):
        return sum(e.amount for e in self.expenses)

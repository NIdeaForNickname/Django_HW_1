class ExpenseController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_expense(self, description, amount):
        self.model.add_expense(description, amount)
        self.view.show_message("Successfully added expense")

    def delete_expense(self, expense_id):
        self.model.delete_expense(expense_id)
        self.view.show_message("Successfully deleted expense")

    def list_expenses(self):
        expenses = self.model.get_all_expenses()
        self.view.show_expenses(expenses)

    def show_total(self):
        total = self.model.get_total()
        self.view.show_total(total)

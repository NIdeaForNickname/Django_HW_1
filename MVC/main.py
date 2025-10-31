from model import ExpenseModel
from view import ExpenseView
from controller import ExpenseController

def main():
    model = ExpenseModel()
    view = ExpenseView()
    controller = ExpenseController(model, view)

    while True:
        print("\n1. Add expense")
        print("2. Remove expense by ID")
        print("3. Show expenses")
        print("4. Show total")

        choice = input("Action: ")

        if choice == '1':
            desc = input("Description: ")
            amount = float(input("Amount: "))
            controller.add_expense(desc, amount)

        elif choice == '2':
            expense_id = int(input("ID: "))
            controller.delete_expense(expense_id)

        elif choice == '3':
            controller.list_expenses()

        elif choice == '4':
            controller.show_total()

if __name__ == "__main__":
    main()

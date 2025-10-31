class ExpenseView:
    def show_expenses(self, expenses):
        if not expenses:
            print("No expenses")
            return
        for e in expenses:
            print(f"ID: {e.id} | {e.description} — {e.amount}")

    def show_total(self, total):
        print(f"\nTotal: {total}")

    def show_message(self, message):
        print(message)

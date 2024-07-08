from datetime import datetime


class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, date=None):
        self.balance += amount
        self.transactions.append({"type": "Income", "amount": amount, "date": date})

    def add_expense(self, amount, category, date=None):
        self.balance -= amount
        self.transactions.append(
            {"type": "Expense", "amount": amount, "category": category, "date": date}
        )

    def view_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def view_transactions(self):
        for transaction in self.transactions:
            if transaction["type"] == "Income":
                print(f"Income: +${transaction['amount']:.2f} on {transaction['date']}")
            elif transaction["type"] == "Expense":
                print(
                    f"Expense: -${transaction['amount']:.2f} ({transaction['category']}) on {transaction['date']}"
                )


def main():
    tracker = BudgetTracker()

    while True:
        print("\nPersonal Budget Tracker - Version 2")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter the income amount: "))
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tracker.add_income(amount, date)
        elif choice == "2":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tracker.add_expense(amount, category, date)
        elif choice == "3":
            tracker.view_balance()
        elif choice == "4":
            tracker.view_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

import json
import os
from datetime import datetime

TRANSACTIONS_FILE = "budget_transactions.json"


class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(TRANSACTIONS_FILE, "r") as file:
                # Check if the file is empty
                file_content = file.read()
                if not file_content:
                    # Initialize an empty list or dictionary if the file is empty
                    self.transactions = []
                else:
                    # If the file is not empty, load the JSON data
                    self.transactions = json.loads(file_content)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty list or dictionary
            self.transactions = []
        except json.JSONDecodeError:
            # Handle other JSON errors (e.g., corrupted file)
            print(
                "Error decoding JSON from transactions file. Initializing empty transactions list."
            )
            self.transactions = []

    def save_transactions(self):
        transactions_data = {"transactions": self.transactions, "balance": self.balance}
        with open(TRANSACTIONS_FILE, "w") as file:
            json.dump(transactions_data, file)

    def add_income(self, amount, date=None):
        self.balance += amount
        self.transactions.append({"type": "Income", "amount": amount, "date": date})
        self.save_transactions()

    def add_expense(self, amount, category, date=None):
        self.balance -= amount
        self.transactions.append(
            {"type": "Expense", "amount": amount, "category": category, "date": date}
        )
        self.save_transactions()

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
        print("\nPersonal Budget Tracker - Version 3")
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

class BudgetTracker:
    def __init__(self):
        self.balance = 0

    def add_income(self, amount):
        self.balance += amount

    def add_expense(self, amount):
        self.balance -= amount

    def view_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")


def main():
    tracker = BudgetTracker()

    while True:
        print("\nPersonal Budget Tracker - Version 1")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter the income amount: "))
            tracker.add_income(amount)
        elif choice == "2":
            amount = float(input("Enter the expense amount: "))
            tracker.add_expense(amount)
        elif choice == "3":
            tracker.view_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from a CSV file."""
        if os.path.isfile(FILENAME):
            with open(FILENAME, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.expenses = [dict(row) for row in reader]
                self.expenses = [{'id': int(e['id']), 'description': e['description'], 'amount': float(e['amount']), 'date': e['date']} for e in self.expenses]
        else:
            self.expenses = []

    def save_expenses(self):
        """Save expenses to a CSV file."""
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ['id', 'description', 'amount', 'date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    def add_expense(self, description, amount, date):
        """Add a new expense."""
        expense_id = max([e['id'] for e in self.expenses], default=0) + 1
        expense = {
            'id': expense_id,
            'description': description,
            'amount': amount,
            'date': date
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def list_expenses(self):
        """List all expenses."""
        if not self.expenses:
            print("No expenses found.")
            return

        print(f"{'ID':<5} {'Description':<20} {'Amount':<10} {'Date':<12}")
        print('-' * 47)
        for expense in self.expenses:
            print(f"{expense['id']:<5} {expense['description']:<20} {expense['amount']:<10.2f} {expense['date']:<12}")

    def show_total_expenses(self):
        """Show total amount of expenses."""
        total = sum(e['amount'] for e in self.expenses)
        print(f"Total Expenses: {total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
                continue
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
                continue
            tracker.add_expense(description, amount, date)
        elif choice == '2':
            tracker.list_expenses()
        elif choice == '3':
            tracker.show_total_expenses()
        elif choice == '4':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()

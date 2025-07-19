import sqlite3
import os
from datetime import datetime

class FinanceManager:
    def __init__(self):
        self.db_file = "finance.db"
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database and create tables"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # Create transactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_income(self, amount, description=""):
        """Add income transaction to database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO transactions (type, amount, description, date)
            VALUES (?, ?, ?, ?)
        ''', ('income', amount, description, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        conn.commit()
        conn.close()
        print(f"Income of ${amount} added successfully!")
    
    def add_expense(self, amount, description=""):
        """Add expense transaction to database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO transactions (type, amount, description, date)
            VALUES (?, ?, ?, ?)
        ''', ('expense', amount, description, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        
        conn.commit()
        conn.close()
        print(f"Expense of ${amount} added successfully!")
    
    def get_balance(self):
        """Calculate and return current balance"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # Get total income
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type = "income"')
        total_income = cursor.fetchone()[0] or 0
        
        # Get total expenses
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type = "expense"')
        total_expenses = cursor.fetchone()[0] or 0
        
        conn.close()
        return total_income - total_expenses
    
    def view_balance(self):
        """Display current balance"""
        balance = self.get_balance()
        print(f"\nCurrent Balance: ${balance:.2f}")
    
    def view_transactions(self):
        """Display all transactions from database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        transactions = cursor.fetchall()
        
        conn.close()
        
        if not transactions:
            print("\nNo transactions found.")
            return
        
        print("\nTransaction History:")
        print("-" * 70)
        print(f"{'ID':<3} {'Date':<20} {'Type':<8} {'Amount':<10} {'Description'}")
        print("-" * 70)
        
        for transaction in transactions:
            id, type_, amount, description, date = transaction
            type_symbol = "+" if type_ == "income" else "-"
            print(f"{id:<3} {date:<20} {type_symbol}{amount:<9.2f} {description}")
    
    def view_summary(self):
        """Display financial summary from database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # Get total income
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type = "income"')
        total_income = cursor.fetchone()[0] or 0
        
        # Get total expenses
        cursor.execute('SELECT SUM(amount) FROM transactions WHERE type = "expense"')
        total_expenses = cursor.fetchone()[0] or 0
        
        # Get transaction counts
        cursor.execute('SELECT COUNT(*) FROM transactions WHERE type = "income"')
        income_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM transactions WHERE type = "expense"')
        expense_count = cursor.fetchone()[0]
        
        conn.close()
        
        net_balance = total_income - total_expenses
        
        print("\nFinancial Summary:")
        print("-" * 40)
        print(f"Total Income: ${total_income:.2f} ({income_count} transactions)")
        print(f"Total Expenses: ${total_expenses:.2f} ({expense_count} transactions)")
        print(f"Net Balance: ${net_balance:.2f}")
        print(f"Total Transactions: {income_count + expense_count}")

def main():
    finance = FinanceManager()
    
    while True:
        print("\n" + "="*50)
        print("FINANCE MANAGEMENT SYSTEM (SQLite3)")
        print("="*50)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. View Summary")
        print("6. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            try:
                amount = float(input("Enter income amount: $"))
                description = input("Enter description (optional): ")
                finance.add_income(amount, description)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        
        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: $"))
                description = input("Enter description (optional): ")
                finance.add_expense(amount, description)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        
        elif choice == "3":
            finance.view_balance()
        
        elif choice == "4":
            finance.view_transactions()
        
        elif choice == "5":
            finance.view_summary()
        
        elif choice == "6":
            print("Thank you for using Finance Management System!")
            break
        
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main() 
# Finance Management System

A simple Python-based finance management system using SQLite3 database to track income, expenses, and maintain financial records.

## Features

- Add income transactions
- Add expense transactions
- View current balance
- View transaction history with transaction IDs
- View financial summary (total income, expenses, and net balance)
- SQLite3 database for reliable data storage
- Transaction counts and detailed reporting

## How to Run

1. Make sure you have Python installed on your system
2. Open terminal/command prompt in the project directory
3. Run the following command:

```bash
python finance_manager.py
```

## Usage

The system provides a simple menu-driven interface:

1. **Add Income** - Enter income amount and optional description
2. **Add Expense** - Enter expense amount and optional description
3. **View Balance** - See current account balance
4. **View Transactions** - Display all transaction history with IDs
5. **View Summary** - Show total income, expenses, transaction counts, and net balance
6. **Exit** - Close the application

## Data Storage

All financial data is automatically saved to `finance.db` SQLite3 database file in the same directory. The database includes:

- **transactions table** with columns:
  - id (auto-incrementing primary key)
  - type (income/expense)
  - amount (decimal value)
  - description (optional text)
  - date (timestamp)

The data persists between sessions and provides better data integrity than file-based storage.

## Requirements

- Python 3.x
- SQLite3 (included with Python by default)

## File Structure

```
Finance_Management/
├── finance_manager.py      # Main application file
├── finance.db              # SQLite3 database file (created automatically)
└── README.md              # This file
```

## Database Features

- **ACID Compliance**: Ensures data integrity
- **Automatic ID Generation**: Each transaction gets a unique ID
- **Efficient Queries**: Fast data retrieval and calculations
- **Data Persistence**: Reliable storage that survives system restarts
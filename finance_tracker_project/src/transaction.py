# transaction.py

# Function to add an income or expense transaction to the list
def add_transaction(transactions, type_, amount, category, date):
    """Add a new transaction to the list."""
    transaction = {
        "type": type_,
        "amount": amount,
        "category": category,
        "date": date
    }
    transactions.append(transaction)
    print("Transaction added successfully!")

# Function to generate a financial summary (total income, total expenses, and savings)
def generate_summary(transactions):
    """Generate a summary of income, expenses, and savings."""
    total_income = 0
    total_expenses = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        elif transaction["type"] == "expense":
            total_expenses += transaction["amount"]

    savings = total_income - total_expenses
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Savings: ${savings}")

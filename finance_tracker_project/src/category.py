# category.py

# Function to break down expenses by category
def category_breakdown(transactions):
    """Show the breakdown of expenses by category."""
    categories = {}

    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
            categories[category] = categories.get(category, 0) + amount  # Accumulate amount for each category

    print("\nExpense Breakdown by Category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

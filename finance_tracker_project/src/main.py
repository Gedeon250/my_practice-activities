# main.py
from transaction import add_transaction, generate_summary
from file_operations import save_data_to_file, load_data_from_file
from category import category_breakdown  # Optional: For category breakdown

def main():
    # Load transactions from file when the program starts
    transactions = load_data_from_file()

    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Category Breakdown")  # Optional
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Get details from the user to add an income
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(transactions, "income", amount, category, date)

        elif choice == '2':
            # Get details from the user to add an expense
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(transactions, "expense", amount, category, date)

        elif choice == '3':
            # Show the summary of income, expenses, and savings
            generate_summary(transactions)

        elif choice == '4':  # Optional category breakdown
            category_breakdown(transactions)

        elif choice == '5':
            # Save the data to the file before exiting
            save_data_to_file(transactions)
            break  # Exit the loop

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

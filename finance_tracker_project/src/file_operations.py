# file_operations.py
import json

# Function to save transactions to a JSON file
def save_data_to_file(transactions, filename="data/transactions.json"):
    """Save the list of transactions to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(transactions, file, indent=4)  # Save with indentation for readability
    print("Data saved to file!")

# Function to load transactions from a JSON file
def load_data_from_file(filename="data/transactions.json"):
    """Load transactions from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Read and return the JSON data
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

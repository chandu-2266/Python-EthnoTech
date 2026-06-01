import json
import os

data_file = os.path.join(os.path.dirname(__file__), "bank_data.json")

def load_bank_data():
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as f:
                data = json.load(f)
                return data.get("balance", 1000), data.get("transactions", [])
        except (json.JSONDecodeError, IOError):
            pass
    return 1000, []

def save_bank_data(account_balance, transactions):
    with open(data_file, "w") as f:
        json.dump({"balance": account_balance, "transactions": transactions}, f)

print("Welcome to the bank!")
account_balance, transactions = load_bank_data()
Transcations=[]
while True:
    print("Please select an option:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"Your current balance is: ${account_balance}")
        
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        account_balance += amount
        transactions.append(f"Deposited: ${amount}")
        save_bank_data(account_balance, transactions)
        print(f"You have deposited ${amount}. Your new balance is: ${account_balance}")
        
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > account_balance:
            print("Insufficient funds!")
        else:
            account_balance -= amount
            transactions.append(f"Withdrew: ${amount}")
            save_bank_data(account_balance, transactions)
            print(f"You have withdrawn ${amount}. Your new balance is: ${account_balance}")
            
    elif choice == "4":
        save_bank_data(account_balance, transactions)
        print("Thank you for banking with us!")
        break
        
    else:
        print("Invalid option, please try again.")
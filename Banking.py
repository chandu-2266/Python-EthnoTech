print("Welcome to the bank!")
account_balance = 1000
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
        Transcations.append(f"Deposited: ${amount}")
        print(f"You have deposited ${amount}. Your new balance is: ${account_balance}")
        
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > account_balance:
            print("Insufficient funds!")
        else:
            account_balance -= amount
            Transcations.append(f"Withdrew: ${amount}")
            print(f"You have withdrawn ${amount}. Your new balance is: ${account_balance}")
            
    elif choice == "4":
        print("Thank you for banking with us!")
        break
        
    else:
        print("Invalid option, please try again.")
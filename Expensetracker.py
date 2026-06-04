
expenses = []
while True:
    print("Please select an option:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total expenses")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        expenses.append({"amount": amount, "category": category})
        print(f"Added expense: ${amount} for {category}")
        
    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for expense in expenses:
                print(f"- ${expense['amount']} for {expense['category']}")
                
    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: ${total}")
        
    elif choice == "4":
        print("Thank you for using the Expense Tracker!")
        break
        
    else:
        print("Invalid option, please try again.")
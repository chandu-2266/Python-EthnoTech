class InsufficientFundsError(Exception):
    pass

class NegativeDepositError(ValueError):
    pass

def deposit(balance, amount):
    if amount < 0:
        raise NegativeDepositError("Deposit amount cannot be negative.")
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Withdrawal amount exceeds current balance.")
    return balance - amount

def main():
    balance = 0.0

    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current balance: ₹{balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                balance = deposit(balance, amount)
                print(f"Deposited ₹{amount:.2f}. New balance: ₹{balance:.2f}")
            except NegativeDepositError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input. Enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                balance = withdraw(balance, amount)
                print(f"Withdrew ₹{amount:.2f}. New balance: ₹{balance:.2f}")
            except InsufficientFundsError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input. Enter a valid number.")
        elif choice == "4":
            print("Thank you for using the ATM simulator.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

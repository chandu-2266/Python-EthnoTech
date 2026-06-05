import math

menu = {
    1: ("Burger", 120.0),
    2: ("Pizza", 250.0),
    3: ("Pasta", 180.0),
    4: ("Sandwich", 90.0),
    5: ("Soft Drink", 50.0)
}

def display_menu():
    print("\n---- Restaurant Menu ----")
    for item_no, (item_name, price) in menu.items():
        print(f"{item_no}. {item_name} - Rs {price:.2f}")
    print("0. Finish order")


def calculate_bill(order):
    subtotal = 0.0
    for item_no, quantity in order.items():
        item_name, price = menu[item_no]
        subtotal += price * quantity
    tax = subtotal * 0.05
    service_charge = subtotal * 0.02
    total = subtotal + tax + service_charge
    rounded_total = math.ceil(total)
    return subtotal, tax, service_charge, rounded_total


def main():
    print("Welcome to the Restaurant Billing System")
    order = {}
    while True:
        display_menu()
        try:
            choice = int(input("Enter item number (0 to finish): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break
        if choice not in menu:
            print("Invalid choice. Try again.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue
        if quantity <= 0:
            print("Quantity must be at least 1.")
            continue

        order[choice] = order.get(choice, 0) + quantity
        print(f"Added {quantity} x {menu[choice][0]} to your order.")

    if not order:
        print("No items ordered. Exiting.")
        return

    subtotal, tax, service_charge, rounded_total = calculate_bill(order)
    print("\n---- Bill Summary ----")
    for item_no, quantity in order.items():
        item_name, price = menu[item_no]
        print(f"{item_name} x {quantity} = Rs {price * quantity:.2f}")
    print(f"Subtotal: Rs {subtotal:.2f}")
    print(f"Tax (5%): Rs {tax:.2f}")
    print(f"Service Charge (2%): Rs {service_charge:.2f}")
    print(f"Total (rounded up): Rs {rounded_total}")


if __name__ == "__main__":
    main()

import random

def play_tambola():
    ticket_numbers = random.sample(range(1, 91), 10)
    print("Your Tambola ticket numbers:", ticket_numbers)

    picks = []
    for i in range(1, 4):
        while True:
            try:
                pick = int(input(f"Pick number {i} (1-90): "))
                if 1 <= pick <= 90:
                    picks.append(pick)
                    break
            except ValueError:
                pass
            print("Enter a valid number between 1 and 90.")
    matches = len(set(picks) & set(ticket_numbers))

    if matches >= 3:
        discount = 20
        print(f"You matched {matches} numbers. You earn a 20% discount!")
    elif matches >= 1:
        discount = 10
        print(f"You matched {matches} numbers. You earn a 10% discount.")
    else:
        discount = 0
        print("No matches this time. No discount earned.")
    return discount

def Ebook_reader():
    books = [
        ("Learning Python", "Python is a versatile language used for many purposes."),
        ("The Discount Shopper", "A smart buyer always seeks the best deal."),
        ("Coding Adventures", "Every project begins with a single line of code.")
    ]

    print("Available e-books:")
    for index, (title, _) in enumerate(books, start=1):
        print(f"{index}. {title}")
    print("4. Go back")

    choice = input("Choose an e-book to read: ")
    if choice in {"1", "2", "3"}:
        index = int(choice) - 1
        title, excerpt = books[index]
        print(f"\nReading '{title}'...\n{excerpt}\n")
        print("You read an e-book and earned a 5% discount on your next purchase.")
        return 5
    print("Returning to main menu.")
    return 0

def ecommerce_app(current_discount):
    products = {
        "1": ("T-shirt", 450),
        "2": ("Jeans", 1200),
        "3": ("Sneakers", 2200)
    }
    cart = []
    while True:
        print("\nE-commerce store:")
        for key, (name, price) in products.items():
            print(f"{key}. {name} - ₹{price}")
        print("4. Checkout")
        choice = input("Enter your choice: ")

        if choice in products:
            cart.append(products[choice])
            print(f"Added {products[choice][0]} to cart.")
        elif choice == "4":
            break
        else:
            print("Invalid option, please try again.")

    if not cart:
        print("Your cart is empty.")
        return

    total = sum(price for _, price in cart)
    final_total = total
    if current_discount > 0:
        final_total = total * (100 - current_discount) / 100
        print(f"\nDiscount applied: {current_discount}%")
    print("\nYour cart:")
    for name, price in cart:
        print(f"- {name}: ₹{price}")
    print(f"Subtotal: ₹{total}")
    print(f"Total after discount: ₹{final_total:.2f}")

def main():
    current_discount = 0
    while True:
        print("\nWelcome to the shop!")
        print("1. Play tambola game to get discount on your next purchase")
        print("2. E-book reader for discount on your next purchase")
        print("3. E-commerce app")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            discount = play_tambola()
            current_discount = max(current_discount, discount)
        elif choice == "2":
            discount = Ebook_reader()
            current_discount = max(current_discount, discount)
        elif choice == "3":
            ecommerce_app(current_discount)
        elif choice == "4":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

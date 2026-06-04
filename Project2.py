import os

CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.txt")


def load_contacts():
    contacts = []
    if not os.path.exists(CONTACTS_FILE):
        return contacts

    with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if "," not in line:
                continue
            name, phone = line.split(",", 1)
            contacts.append({"name": name.strip(), "phone": phone.strip()})
    return contacts


def save_contact(name, phone):
    with open(CONTACTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{phone}\n")


def add_new_contact():
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Phone number cannot be empty.")
        return

    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return

    save_contact(name, phone)
    print(f"Contact '{name}' added successfully.")


def search_contact():
    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return

    contacts = load_contacts()
    matches = [c for c in contacts if query in c["name"].lower()]

    if not matches:
        print(f"No contacts found matching '{query}'.")
        return

    print("\nSearch Results:")
    for contact in matches:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")


def display_all_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    contacts.sort(key=lambda c: c["name"].lower())
    print("\nAll Contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")


def print_menu():
    print("\nContact Book")
    print("1. Add New Contact")
    print("2. Search Contact by Name")
    print("3. Display All Contacts")
    print("4. Exit Program")


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_new_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_all_contacts()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()

import importlib

print("\n----miniproject----")

MODULE_MAP = {
    "1": ("Banking", "Banking"),
    "2": ("Student", "Student"),
    "3": ("Expense Tracker", "Expensetracker"),
    "4": ("Chatbot AI", "ChatboatAi"),
}

def call_entry(module):
    # try common entry function names in order
    for name in ("main", "start_chat", "start", "run"):
        func = getattr(module, name, None)
        if callable(func):
            func()
            return True
    return False

def main():
    while True:
        print("\n1. Banking")
        print("2. Student")
        print("3. Expense Tracker")
        print("4. Chatbot AI")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice in MODULE_MAP:
            display_name, module_name = MODULE_MAP[choice]
            try:
                module = importlib.import_module(module_name)
            except ModuleNotFoundError:
                print(f"Error: module '{module_name}' not found.")
                continue
            except Exception as e:
                print(f"Error importing '{module_name}': {e}")
                continue

            try:
                if not call_entry(module):
                    print(f"Module '{module_name}' has no callable entry function (main/start_chat/start/run).")
            except Exception as e:
                print(f"Error while running '{module_name}': {e}")

        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

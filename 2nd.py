file_name = input("Enter file name to read: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        print("\nFile content:\n")
        print(file.read())
except FileNotFoundError:
    print(f"File not found: {file_name}")
except PermissionError:
    print(f"Permission denied: {file_name}")
except Exception as e:
    print(f"An error occurred: {e}")

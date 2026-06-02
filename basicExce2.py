while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid integers.")

print(f"\nYou entered: {a} and {b}")
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
try:
    print(f"Division: {a / b}")
except ZeroDivisionError:
    print("Cannot divide by zero.")

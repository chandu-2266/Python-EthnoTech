class AgeValidationError(ValueError):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise AgeValidationError("Age must be between 0 and 120.")
    return True

def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            validate_age(age)
            print(f"Age {age} is valid.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except AgeValidationError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

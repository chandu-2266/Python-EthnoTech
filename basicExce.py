a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
try:
    print(a/b)
except (ZeroDivisionError):
    print("try another:")
except (ValueError):
    print("try another:")
else:
    print(a/b)
finally:
    print("This will always execute.")
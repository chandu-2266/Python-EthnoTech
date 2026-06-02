a=[5, 10, 15]
print(a[1])
try:
    print(a[3])
except IndexError:
    print("Index out of range!")
except TypeError:
    print("Invalid operation!")
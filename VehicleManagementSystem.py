class Vehicle:
    def __init__(self, name: str, brand: str, price: float):
        self.name = name
        self.brand = brand
        self.price = price

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: Rs {self.price:.2f}")


class Car(Vehicle):
    def __init__(self, name: str, brand: str, price: float, doors: int = 4):
        super().__init__(name, brand, price)
        self.doors = doors

    def display_details(self):
        super().display_details()
        print(f"Doors: {self.doors}")


class Bike(Vehicle):
    def __init__(self, name: str, brand: str, price: float, engine_cc: int = 150):
        super().__init__(name, brand, price)
        self.engine_cc = engine_cc

    def display_details(self):
        super().display_details()
        print(f"Engine: {self.engine_cc} cc")


class SportsCar(Car):
    def __init__(self, name: str, brand: str, price: float, doors: int = 2, top_speed: int = 250):
        super().__init__(name, brand, price, doors)
        self.top_speed = top_speed

    def display_details(self):
        super().display_details()
        print(f"Top Speed: {self.top_speed} km/h")


def input_vehicle_data():
    name = input("Enter vehicle name: ").strip()
    brand = input("Enter brand: ").strip()
    price = float(input("Enter price: ").strip())
    return name, brand, price


def add_car(cars):
    print("\nAdd Car")
    name, brand, price = input_vehicle_data()
    doors = int(input("Enter number of doors: ").strip())
    cars.append(Car(name, brand, price, doors))
    print("Car added.\n")


def add_bike(bikes):
    print("\nAdd Bike")
    name, brand, price = input_vehicle_data()
    engine_cc = int(input("Enter engine CC: ").strip())
    bikes.append(Bike(name, brand, price, engine_cc))
    print("Bike added.\n")


def add_sports_car(sports_cars):
    print("\nAdd SportsCar")
    name, brand, price = input_vehicle_data()
    top_speed = int(input("Enter top speed (km/h): ").strip())
    sports_cars.append(SportsCar(name, brand, price, doors=2, top_speed=top_speed))
    print("SportsCar added.\n")


def show_list(items, title):
    print(f"\n--- {title} ---")
    if not items:
        print("No items to show.")
        return

    for index, item in enumerate(items, start=1):
        print(f"\n{index}.")
        item.display_details()


def demonstrate_inheritance():
    print("\n--- Inheritance Demonstration ---")

    print("\n1. Single Inheritance")
    car = Car("Sedan", "Toyota", 1200000.0, doors=4)
    bike = Bike("Hawk", "Honda", 95000.0, engine_cc=160)
    car.display_details()
    print()
    bike.display_details()

    print("\n2. Multilevel Inheritance")
    sports_car = SportsCar("Coupe", "BMW", 3500000.0, doors=2, top_speed=300)
    sports_car.display_details()

    print("\n3. Hierarchical Inheritance")
    print("Both Car and Bike inherit from Vehicle:")
    vehicles = [car, bike, sports_car]
    for index, vehicle in enumerate(vehicles, start=1):
        print(f"\nVehicle {index}:")
        vehicle.display_details()


def main():
    cars = []
    bikes = []
    sports_cars = []

    while True:
        print("\nVehicle Management Menu")
        print("1. Add Car")
        print("2. Add Bike")
        print("3. Add SportsCar")
        print("4. Show Car Details")
        print("5. Show Bike Details")
        print("6. Show SportsCar Details")
        print("7. Demonstrate Inheritance")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_car(cars)
        elif choice == "2":
            add_bike(bikes)
        elif choice == "3":
            add_sports_car(sports_cars)
        elif choice == "4":
            show_list(cars, "Car Details")
        elif choice == "5":
            show_list(bikes, "Bike Details")
        elif choice == "6":
            show_list(sports_cars, "SportsCar Details")
        elif choice == "7":
            demonstrate_inheritance()
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
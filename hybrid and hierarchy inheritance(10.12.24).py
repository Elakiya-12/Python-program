#question hybrid inheritance
# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_vehicleInfo(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Car class
class Car(Vehicle):
    def __init__(self, make, model, year, doors, trunk_cap):
        Vehicle.__init__(self, make, model, year)  # Explicitly initialize Vehicle
        self.doors = doors
        self.trunk_cap = trunk_cap
    def display_features(self):
        print(f"Doors: {self.doors}, Trunk Capacity: {self.trunk_cap} liters")

# Truck class
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        Vehicle.__init__(self, make, model, year)  # Explicitly initialize Vehicle
        self.cargo_capacity = cargo_capacity

# Hybrid class
class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, doors, cargo_capacity):
        Car.__init__(self, make, model, year, doors, trunk_cap=0)  # trunk_cap defaulted to 0
        Truck.__init__(self, make, model, year, cargo_capacity)  # Explicitly initialize Truck

    def display_features(self):
       print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nDoors: {self.doors}\nCargo Capacity: {self.cargo_capacity} kg")

# Example usage
truck = PickupTruck("Rangerover", "plugIn hybrid p550e", 2023, 4, 1000)
truck.display_features()


#question 2 hierarchial inheritance
# Base class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}\n"
              f"Name: {self.name}\n"
              f"Price: ${self.price:.2f}")

# Derived class for Electronics
class Electronics(Product):
    def __init__(self, product_id, name, price, warranty_period, brand):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period} years\n"
              f"Brand: {self.brand}")

# Derived class for Clothing
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}\n"
              f"Material: {self.material}")

# Example usage
print("Electronics Product:")
laptop = Electronics(product_id="E101", name="Laptop", price=85,000, warranty_period=2, brand="HP")
laptop.display_info()

print("\nClothing Product:")
shirt = Clothing(product_id="C201", name="T-Shirt", price=25.00, size="M", material="Cotton")
shirt.display_info()





















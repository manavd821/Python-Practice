# basic
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand}, {self.model}"
    def __repr__(self):
        return f"Car = '{self.brand}'"
# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# basic
my_car = Car("Toyato", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

# inheritance
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.brand)
print(my_tesla.full_name())
print(my_car)
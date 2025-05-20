# basic
class Car:
    total_car = 0;

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1 
        # self.total_car +=1

    def full_name(self):
        return f"{self.__brand}, {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diseal"
    
    # static method
    @staticmethod
    def general_description():
        return "It is car bhai"
    @property
    def brand(self):
        return self.__brand

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"


# basic
my_car = Car("Toyato", "Corolla")

# inheritance and polymorphism
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_car.fuel_type())
print(my_tesla.fuel_type())
#  calculate number of object
test = Car("ok","ok")
print(Car.total_car) # it include child class too
# print(test.total_car)
# print(my_car.total_car)

# print(my_car.general_description()) object can't excess static method
print(Car.general_description())
print(ElectricCar.general_description()) # child can also access the static method of parent

new_car = Car("safari", "ABC")
# new_car.brand = "city"
print(new_car.brand)

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.__brand}, {self.__model}"
    
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    
# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car("Toyato", "Corolla")
tesla = ElectricCar("Tesla", "Models S", "85kWh")
print(tesla.full_name())
print(my_car.get_brand())

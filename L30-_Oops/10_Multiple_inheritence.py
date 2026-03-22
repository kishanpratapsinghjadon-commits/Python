# PROBLEM = Create two classe battery and engine and let the electriccar class inherit from both , demonstrate multiple inheritance.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

    def get_info(self):
        return f"this is a {self.model} of {self.brand}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
        
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model) # super() is a built-in function in Python that is used to call a method from the parent class. It is often used in the __init__ method of a child class to call the __init__ method of the parent class and initialize the attributes of the parent class.
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electricity"
        
# new_car = Car("Toyota", "Corolla")    
# my_car = ElectricCar("Tesla", "Model S", 100)
# print(my_car.get_info())
# print(my_car.fuel_type())

class Battery:
    def battery_info(self):
        return "this is a battery"
class Engine:
    def engine_info(self):
        return "this is an engine"
    
class ElectricCarTwo(Battery, Engine, Car):
    pass
my_electric_car = ElectricCarTwo("Tesla", "Model 3")
print(my_electric_car.battery_info())
print(my_electric_car.engine_info())
print(isinstance(my_electric_car, Car))     # this will return True because my_electric_car is an instance of the Car class
print(isinstance(my_electric_car, Battery)) # this will return True because my_electric_car is an instance of the Battery class
print(isinstance(my_electric_car, Engine))  # this will return True because my_electric_car is an instance of the Engine class
# Problem : demonstrate polymorphism by defining a method fuel_type in both car and electric car classes , but with different behaviours.
from pyexpat import model


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

    def get_info(self):
        return f"this is a {self.model} of {self.brand}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
        
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # super() is a built-in function in Python that is used to call a method from the parent class. It is often used in the __init__ method of a child class to call the __init__ method of the parent class and initialize the attributes of the parent class.
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"
        
new_car = Car("Toyota", "Corolla")    
my_car = ElectricCar("Tesla", "Model S", 100)
print(my_car.fuel_type())
print(new_car.fuel_type())
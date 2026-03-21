#  problem : Create a class called "Car" with attributes "brand" and "model". Then create a subclass called "ElectricCar" that inherits from the "Car" class and has an additional attribute called "battery_size". Finally, create an object of the "ElectricCar" class and print out all its attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

    def get_info(self):
        return f"this is a {self.model} of {self.brand}"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # super() is a built-in function in Python that is used to call a method from the parent class. It is often used in the __init__ method of a child class to call the __init__ method of the parent class and initialize the attributes of the parent class.
        self.battery_size = battery_size
        
    
my_car = ElectricCar("Tesla", "Model S", 100)
print(my_car.get_info())      
print(my_car.battery_size)
print(my_car.brand)

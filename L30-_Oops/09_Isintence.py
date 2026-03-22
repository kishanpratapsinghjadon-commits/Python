# Problem = demonstrate the use of isinstance() to check if my_car1 is an instance of car and electric_car classes.  
#isinstance() is a built-in function in Python that is used to check if an object is an instance of a specific class or a subclass of that class. It takes two arguments: the object to be checked and the class or tuple of classes to check against. It returns True if the object is an instance of the specified class or a subclass of it, and False otherwise.
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
print(isinstance(my_car, Car)) # this will return True because my_car is an instance of the Car class
print(isinstance(my_car, ElectricCar)) # this will return True because my_car is an instance of the ElectricCar class
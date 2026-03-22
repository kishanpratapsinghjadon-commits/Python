# problem = use a property decorator i the car class to make the model attribute read-only. This means that once a car object is created, the model attribute cannot be changed.

class Car:
    number_of_cars = 0 # class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.brand = brand
        self._model = model # we use a private variable to store the model attribute
        Car.number_of_cars += 1 # increment the class variable when a new car is created

    @property # this is a decorator that is used to define a property in a class. A property
    def model(self):
        return self._model # we return the value of the private variable
my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Honda", "Civic")
my_car3 = Car("Ford", "Mustang")
print("Number of cars created:", Car.number_of_cars)
print("Model of my car 1:", my_car1.model)
print("Model of my car 2:", my_car2.model)
print("Model of my car 3:", my_car3.model)
# my_car1.model = "Camry" # this will raise an error because the model attribute is read-only
print("Updated model of my car 1:", my_car1.model) # this will still print the original model because the model attribute is read-only and cannot be changed.
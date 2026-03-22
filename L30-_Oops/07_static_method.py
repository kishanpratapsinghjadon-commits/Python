# Problem = add a static method to the car class that returns a general description of a car.
# this wil acsses the class not object, so we can call it without creating an instance of the class. We can call it directly on the class itself.

class Car:
    number_of_cars = 0 # class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.number_of_cars += 1 # increment the class variable when a new car is created

    @staticmethod #this is a decorator that is used to define a static method in a class. A static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class.
    def car_description():
        return "A car is a vehicle that is used for transportation."
my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Honda", "Civic")
my_car3 = Car("Ford", "Mustang")
print("Number of cars created:", Car.number_of_cars)
print(Car.car_description())
#we can change the object attributes, like the model attribute, but we cannot change the static method because it belongs to the class, not the object.
my_car1.model = "Camry" # this will work because the model attribute is not read-only
print("Updated model of my car 1:", my_car1.model)
# Problem = add a class variables to the car that keeps track the number of cars created.
class Car:
    number_of_cars = 0 # class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.number_of_cars += 1 # increment the class variable when a new car is created
my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Honda", "Civic")
my_car3 = Car("Ford", "Mustang")
print("Number of cars created:", Car.number_of_cars)

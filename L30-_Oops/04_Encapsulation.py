#problem = modify the car class to encapsulate the brand attribute , making it private,and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
            return self.__brand + " is the brand of the car"
my_car = Car("Tesla", "Model S")
print(my_car.__brand())# it will give an error because __brand is a private attribute and cannot be accessed directly from outside the class

# print(my_car._Car__brand) # it will give an error because __brand is a private attribute and cannot be accessed directly from outside the class 


        
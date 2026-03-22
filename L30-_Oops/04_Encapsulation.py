#problem = modify the car class to encapsulate the brand attribute , making it private,and provide a getter method for it.
# Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. In this case, we will make the brand attribute private by prefixing it with double underscores (__), and we will provide a getter method called get_brand() to access the value of the brand attribute.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
            return self.__brand + " is the brand of the car"
my_car = Car("Tesla", "Model S")
print(my_car.__brand_brand())# it will give an error because __brand is a private attribute and cannot be accessed directly from outside the class
print(my_car.get_brand()) # this will work because we are taking info form the object using the getter method provided by the class, which is the recommended way to access private attributes.
# print(my_car._Car__brand) # it will NOT give an error because __brand is a private attribute but we can access it using the name mangling syntax _ClassName__attributeName. However, it is not recommended to access private attributes in this way as it goes against the principle of encapsulation. It is better to use the getter method provided by the class to access the value of the private attribute.


        
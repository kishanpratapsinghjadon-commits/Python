class Employee:

    def __init__(self, name, age, bond):
        self.name = name # self is a reference to the current object. It is used to access the attributes and methods of the class in python. It is a convention to use self as the name for the first parameter of a method in a class, but it can be named anything else as well.
        self.age = age
        self.bond = bond

    def get_info(self):
     print(f"The name of the employee is {self.name}. age of the employee is {self.age} and bond period is {self.bond} years")
e1 = Employee("John Doe", 30, 5) # An object of class Employee is crearted here
e1.get_info() # Employee e1's get info method is called for the first object here
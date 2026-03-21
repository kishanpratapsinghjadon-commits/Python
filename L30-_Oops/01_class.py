# class: Class is a blueprint or a template. Eg. form for an exam that contains name, age, electives, father's name etc

# object: specific instance created from the template (class.). Eg. form which contains the data for john doe

class Employee:
    company = "HP"

    def get_salary(self): # self is important because self is a way to refrence the current object. It is used to access the attributes and methods of the class in python. It is a convention to use self as the name for the first parameter of a method in a class, but it can be named anything else as well.
        print(self) # self is a reference to the current object. It is used to access the attributes and methods of the class in python. It is a convention to use self as the name for the first parameter of a method in a class, but it can be named anything else as well.
        return 34000
    

e = Employee() # An object of class Employee is crearted here
print(e.get_salary()) # Employee e's get salary method is called for the first object here

company = "Microsoft" #it is a local variable and cannot change comapny variable

e2 = Employee() # Another object of class Employee is created here
print(e2.get_salary()) # Employee e2's get salary method is called for the second object here

print(e2.company) # due to local variable comapny it will not print microsoft but it will print HP which is the global variable of class Employee

# another class is created here
class Owner:
    company = "Khudki"
    def have_share(self):
        print(self) # self is a reference to the current object. It is used to access the attributes and methods of the class in python. It is a convention to use self as the name for the first parameter of a method in a class, but it can be named anything else as well.
        return 90
    
o = Owner()
print(o.have_share())
    
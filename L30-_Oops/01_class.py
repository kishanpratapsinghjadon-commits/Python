# class: Class is a blueprint or a template. Eg. form for an exam that contains name, age, electives, father's name etc

# object: specific instance created from the template (class.). Eg. form which contains the data for john doe

class Employee:
    company = "HP"

    def get_salary(self):
        return 34000
    

e = Employee() # An object of class Employee is crearted here
print(e.get_salary()) # Employee's get salary method is called
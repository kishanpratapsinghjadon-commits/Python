def sum(a, b):
    # a and b are local variable-- can be accessed only inside the function not outside
    c = a + b
    z = 1 #it creartes a local variable called z which is destroyed after this function returns
    return c
def greet():
    z = 32 # Local variable or local scope
    print("hello")

z = 8 # z is a global variable or global scope
print(sum(4, 6))
print(z)
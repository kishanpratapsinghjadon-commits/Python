#problem = create a decorator to print the function name and the values of its arguments every time thye functon is called.
def debug(func):
    def wrapper(*args ,**kwargs):
        args_values= ',' .join(str(arg) for arg in args)
        kwargs_values = ','.join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling {func.__name__} with arguments: {args_values} and keyword arguments: {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper

@debug
def example_function(a, b, c=0):
    return a + b + c   
print(example_function(1, 2, c=3))

@debug
def greeting(name, greeting="Hello"):
    return f"{greeting} {name}"
print(greeting("Alice"))
print(greeting("Bob", greeting="Hi"))
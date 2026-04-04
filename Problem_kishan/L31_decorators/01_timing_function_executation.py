#problem = write a decorator that measures the time a function takes to execute.
import time 
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time() # this will give us the current time in seconds since the epoch
        result = func(*args, **kwargs) # this will call the original function and store the result
        end = time.time() # this will give us the current time in seconds since the epoch
        print(f"{func.__name__} took {end - start} seconds to execute.")
        return result
    return wrapper

@timer #now this will pass the any function from the timer function and it will be decorated with the timer functionality
def example_function(n):
    time.sleep(n)

example_function(2)

































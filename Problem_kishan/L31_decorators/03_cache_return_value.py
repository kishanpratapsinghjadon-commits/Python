#problem = implement a decorator that caches the return values of a function , so that when it's called with tyhe same arguments, the cache value is returned instead of re-executing the function.
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper



@cache
def long_running_function(a,b):
    time.sleep(4)  # Simulate a long-running operation
    return a + b

print(long_running_function(2,3))  # This will take 4 seconds to execute   
print(long_running_function(4,5))  # This will take 4 seconds to execute
print(long_running_function(2,3))  # This will return the cached value immediately
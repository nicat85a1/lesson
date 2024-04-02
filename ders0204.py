"""def list_numbers(n):
    for i in range(n):
        yield i
a = list_numbers(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))"""

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    return wrapper

@timing_decorator
def some_function():
    time.sleep(1)
    return "Hello Word!"
        
print(some_function())
#print(timing_decorator(some_function)())
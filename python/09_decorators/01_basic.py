from functools import wraps

# decorator function
def my_decorators(func):
    @wraps(func)                 # keeps original function name & doc
    def wrapper():
        print("Before function run")  # runs before function
        func()                         # call original function
        print("After functio run")     # runs after function
    return wrapper

print("\n")

@my_decorators                     # apply decorator
def greet():
    print("-> Hello from chiacode")

greet()                            # call decorated function
print(greet.__name__)              # shows original name due to @wraps
print("\n")

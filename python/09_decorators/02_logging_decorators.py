from functools import wraps

# Decorator to log activity of any function
def log_activity(func):
    @wraps(func)  # preserves the original function's name, docstring, etc.
    def wrapper(*args, **kwargs):  # wrapper can take any number of arguments
        print(f"🚀 Calling: {func.__name__}")  # runs before the function
        result = func(*args, **kwargs)        # execute the original function
        print(f"✅ Finished: {func.__name__}") # runs after the function
        return result                          # return whatever the original function returns
    return wrapper  # return the wrapper function

@log_activity  # apply the decorator
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status '{milk}'")  # the main function logic

brew_chai("masala chai")  # call the decorated function

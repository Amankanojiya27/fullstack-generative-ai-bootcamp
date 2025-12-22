from functools import wraps

# Decorator to restrict access to admins only
def required_admin(func):
    @wraps(func)  # preserves original function metadata
    def wrapper(user_role):
        if user_role != "admin":  # check user role
            print("Access denied: Admin only")  # deny access if not admin
            return None
        else:
            return func(user_role)  # call the original function if admin
    return wrapper

@required_admin  # apply the decorator
def access_the_inventory(role):
    print("Access granted to tea inventory")  # only runs for admin

# Test with different roles
access_the_inventory("user")   # should deny access
access_the_inventory("admin")  # should grant access

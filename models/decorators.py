import re


def validate_method_name(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        if not re.match(r'^[a-z_][a-z0-9_]*$', method_name):
            raise ValueError("Invalid method name. Use snake_case naming convention.")
        return func(*args, **kwargs)

    return wrapper

import re
from functools import wraps
import logging


def validate_method_name(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        if not re.match(r'^[a-z_][a-z0-9_]*$', method_name):
            raise ValueError("Invalid method name. Use snake_case naming convention.")
        return func(*args, **kwargs)

    return wrapper


def logged(exception, mode):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger()
                if mode == "console":
                    logger.addHandler(logging.StreamHandler())
                elif mode == "file":
                    logger.addHandler(logging.FileHandler("log.txt"))
                logger.exception(e)

        return wrapper

    return decorator
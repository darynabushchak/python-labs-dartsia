import logging
from functools import wraps


class RedundantHeightException(Exception):
    pass


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
                logger.exception(str(e))

        return wrapper

    return decorator

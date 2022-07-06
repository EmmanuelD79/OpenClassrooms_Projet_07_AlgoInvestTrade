from time import time
from functools import wraps


def count_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        name = func.__name__
        stop = time()
        duration = stop - start
        return result, [name, duration]
    return wrapper

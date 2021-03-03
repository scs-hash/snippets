import time
from functools import wraps

class Timeit:
    """implement decorator with class"""
    def __init__(self, prefix):
        self.prefix = prefix
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(f"{self.prefix} duration time: {end - start}")
        return wrapper

@Timeit('prefix')
def hello():
    time.sleep(1)
    print("hello world")

hello()
import time
from functools import wraps

def timeit(prefix):
    def decorator(func):
        # After decorator ,func.__name__ -> wrapper;
        # @wraps will reset func.__name__ -> normal function name
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(f"{prefix}: duration time: {end - start}")
        return wrapper
    return decorator

@timeit('[This is a prefix string]')
def hello(name):
    time.sleep(1)
    print(f"hello, {name}")

hello('csc')
print(hello.__name__)
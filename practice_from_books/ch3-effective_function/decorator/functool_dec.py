import functools
import time

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() using {args}, {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"TRACE: {func.__name__}() returned result {original_result!r}")
        return original_result
    return wrapper

@trace
def say(name, line):
    """
Me hu bulla, rahta hu khulla
    """
    print(f"TRACE: calling say here brother")
    return f'{name}: {line}'

# print(say.__name__)
# print(say.__doc__)

# caching
@functools.lru_cache(maxsize=100)
def slow_square(n):
    print("start")
    time.sleep(2)
    print("end")
    return n*n

# print(slow_square(2000))
# print(slow_square(2000))

def power(base, exp):
    return base ** exp

# To bind some fix argument to the existing function
square = functools.partial(power, exp = 2)
cube = functools.partial(power, exp = 3)

print(square(3))
print(cube(3))
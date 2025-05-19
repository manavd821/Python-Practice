# import time
# def timer(func):
#     def wrapper(*args, **krargs):
#         start = time.time()
#         result = func(*args, **krargs)
#         end = time.time()
#         print(f"{func.__name__} is execuated in {end-start} time!")
#         return result
#     return wrapper

# def greet(name,n=2):
#     time.sleep(n)
# greet = timer(greet)

# greet("Manav", 2)

# # or use decorator => niche

# @timer
# def greet(name, n=2):
#     time.sleep(n)

# greet("Manav", 2)

# # another example
# # calculate number of arguments and kwargs

def calculate(func):
    def wrapper(*args, **kwargs):
        args_value = ', '. join(str(arg) for arg in args) 
        kwargs_value = ', '.join(f"{key} : {value}" for key, value in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@calculate
def func( name, greeting = "hello"):
    print(f"After Decorator : Hare Krsna, {name} !")

func("manav", greeting = "Hello")
func("Manav")
# def strong(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             print(arg, end=" ")
#         for key, val in kwargs.items():
#             print(key + ' : ' + val)
#         return "<strong>" + func(*args, **kwargs) + "</strong>"
#     return wrapper

# def emphasis(func):
#     def wrapper(*args, **kwargs):
#         # for arg in args:
#         #     print(arg, end=" ")
#         # for key, val in kwargs.items():
#         #     print(key + ' : ' + val)
#         return '<em>' + func(*args, **kwargs) + '</em>'
#     return wrapper

# @strong
# @emphasis
# def greet(name, abcd,sname, rname):
#     return name + sname

# print(greet("Manav", "nnnn",sname= "desai", rname="Hahah"))

def trace(func):
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

print(say("manav", "Hare Krsna"))

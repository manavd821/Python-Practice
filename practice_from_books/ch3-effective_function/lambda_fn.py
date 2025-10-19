from typing import Callable

def make_adder(n : int) -> Callable:
    return lambda x: x + n

adder_3 = make_adder(n=3)
print(adder_3(2))
print(make_adder(5)(3))

print(
    (lambda x,y : x-y)(10,3)
)

uppercase_str_list = map(lambda x : x.upper(), ['manav','desai','hare','krsna'])
print(' '.join(uppercase_str_list))

filter_even_number = list(filter(lambda x : x % 2 == 0, range(0,11)))
print(filter_even_number)
sorted_list = sorted(range(-5,6),key=lambda x : x*x)
print(sorted_list)
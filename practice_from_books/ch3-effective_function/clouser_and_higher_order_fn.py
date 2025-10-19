from ast import Add
from typing import Annotated, Callable


def yell(text : str) -> str:
    return text.upper() 

str_ = list(map(yell,('Manav','desai')))
print(str_) 
print(' '.join(str_))

add = lambda a,b,c : a+b+c
ans = list(map(add, [1,2,3,4],[5,6,7,8],[1,2,3,4]))
                   # ^         ^         ^
print(ans)

def get_speak_func(volume : float) -> Callable:
    def whisper(text : str) -> str:
        return text.lower()
    def yell(text : str) -> str:
        return text.upper()
    return yell if volume > 0.5 else whisper

fn = get_speak_func(0.6)
print(fn('ManaV'))

# clousers : method:1
def make_adder(n : Annotated[int,'Which adder you want to make']) -> Callable:
    def add(x : int) -> int:
        return x + n
    return add

adder_3 = make_adder(n=3)
print(adder_3(2))
print(make_adder(5)(3))

# clousers : method:2
class Adder:
    def __init__(self, n : int):
        self.n = n

    def __call__(self, x):
        return x + self.n
    
adder_3 = Adder(3)
print(adder_3(2))
print(Adder(5)(3))
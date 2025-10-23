import itertools
import numbers
from tkinter.font import names
from tracemalloc import stop
from turtle import st

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4]
names = ['Alice', 'Bob', 'Charlie', 'Diana']

combinations = itertools.combinations(letters, 2)
# for item in combinations:
#     print(item)
    
permutations = itertools.permutations(letters, 2)
# for item in permutations:
#     print(item)

chain = itertools.chain(letters, numbers)
# for item in chain:
#     print(item, end=" ")

islice = itertools.islice(range(10), 5)
# print(list(islice))
square = itertools.starmap(
    pow,
    itertools.islice(zip(itertools.count(),itertools.repeat(2)), 9)
)
# print(list(square))

selectors = [True, False, True, False, True, False, ]
compress_ = itertools.compress(letters, selectors)
# print(list(compress_))

dropwhile_ = itertools.dropwhile(lambda x : x != 3, range(10))
print(list(dropwhile_))

takewhile_ = itertools.takewhile(lambda x : x != 3, range(10))
print(list(takewhile_))

accumulate_ = itertools.accumulate(numbers)
# print(list(accumulate_))
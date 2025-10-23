import itertools    
counter = itertools.count()

data = [100,200,300,400,500]

# zip takes all iteratables and iterate over one by one simultaneously on all and continues until the shortest argument is exhausted.
# The zip object yields n-length tuples, where n is the number of iterables
# passed as positional arguments to zip(). The i-th element in every tuple
# comes from the i-th iterable argument to zip(). This continues until the
# shortest argument is exhausted.
daily_data = list(zip(itertools.count(), data))
# print(daily_data)

# Return a zip_longest object whose .__next__() method returns a tuple where the i-th element comes from the i-th iterable argument. The .__next__() method continues until the longest iterable in the argument sequence is exhausted and then it raises StopIteration. When the shorter iterables are exhausted, the fillvalue is substituted in their place. The fillvalue defaults to None or can be specified by a keyword argument.

# Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.

cycle = itertools.cycle([1,2,3])
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

repeat_ = itertools.repeat(2)
# print(next(repeat_))
# print(next(repeat_))
# print(next(repeat_))
# print(next(repeat_))
# print(next(repeat_))
# print(next(repeat_))

map_ = map(pow, range(11), itertools.repeat(2))
# print(list(map_))

square = map(pow, range(10), itertools.repeat(2))
# print(list(square))

starmap_ = itertools.starmap(pow, [(0,2), (1,2), (2,2), (3,2),])
# print(next(starmap_))
# print(next(starmap_))
# print(next(starmap_))

zip_ = zip(itertools.count(),[0,1,2,3,4])
# print(list(zip_))
# for i, j in zip_:
#     print(i,j)

filter_ = filter(lambda x : not x % 2, range(10))
# print(list(filter_))

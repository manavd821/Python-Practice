# Iterable : something which can loop over -> has one method : iter()
# iterator : actual object that can produce one value at a time -> has two method : iter() and next()

li = [1,2,3]
it = iter(li)

# print(next(it))
# print(next(it))
# print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        break
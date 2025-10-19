# names = ["Krishna", "Radha", "Balaram", "Gopal"]
# names.sort(key=len)
# print(names)

# names = ["Krishna", "Radha", "Balaram", "Gopal"]
# new_name = sorted(names,key=len)
# print(names)
# print(new_name)

# names = ["Krishna", "Radha", "Balaram", "Gopal"]
# new_name = sorted(names, key = lambda x : x[0])
# print(new_name)

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
new_tuples = sorted(tuples, key=lambda x: x[1])
print(new_tuples)

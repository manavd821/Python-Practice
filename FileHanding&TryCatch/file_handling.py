# f1 = open(file='myfile1.txt', mode='r')
# f2 = open(file='myfile2.txt', mode='w')
# f3 = open(file='myfile3.txt', mode='a')

with open(file='myfile1.txt', mode='r') as f1, \
     open(file='myfile2.txt', mode='w+') as f2, \
     open(file='myfile3.txt', mode='a+') as f3:
    
    content = f1.read()
    # print(content)
    f2.write(content)
    f3.write(content)
    f2.seek(0)
    # line = f2.readline()

    while True:
        line = f2.readline()
        if not line: break
        print(line)
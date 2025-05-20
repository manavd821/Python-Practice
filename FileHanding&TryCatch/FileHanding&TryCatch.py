file = open('ok.py','w')
try:
    file.write("Hare Krsna")
finally:
    file.close()

# or

with open('pk.py','w') as file2:
    file2.write("Hare Ram")
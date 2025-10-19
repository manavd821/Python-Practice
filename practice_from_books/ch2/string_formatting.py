name = 'Manav'
surname = 'Desai'

# old style
greet1 = 'Hare Krsna, %s %s' %(name, surname)
print(greet1)

greet2 = 'Hare Krsna, %(name)s %(surname)s' %({
    'name' : name,
    'surname' : surname,
})
print(greet2)

# new style
greet3 = 'Hare Krsna, {name} {surname}'.format(name=name, surname=surname)
print(greet3)

# literal string interpolation
greet4 = f'Hare Krsna, {name} {surname}'
print(greet4)

# Template string
from string import Template
t = Template('Hare Krsna, $name $surname')
greet5 = t.substitute(name = name, surname = str(surname))
print(greet5)
print(Template('Hare Krsna, $name $surname').substitute(name = name, surname = str(surname)))

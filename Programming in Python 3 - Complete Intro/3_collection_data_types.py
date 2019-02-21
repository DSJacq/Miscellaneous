import math
import collections
import sys
import string
import os

print('-------------------------------------------------- Sequence Types')
'''
bytearray
bytes
list
str
typle
'''
#   Tuples

hair = 'black', 'brown', 'blond', 'red'
print(hair[2])
print(hair[-3:])
print(hair[1:])
print(hair[:2])
print(hair[2:])

a,b = (1,2)
del a, b

def f(x):
    return x, x ** 2

for x, y in ((1,1), (2,4),(3,9)):
    print(x,y)

eyes = ('brown','hazel','amber','green','blue','gray')
colors = (hair, eyes)
print(colors[1][3:-1])

things = (1, -7.5, ('pea', (5, 'Xyz'), 'queue'))
print(things[2][1][1][2])

manufacturer, model, seating = (0, 1, 2)
minimum, maximum = (0,1)
aricraft = ('Airbus', 'A320-200', (100, 200))
print(aricraft[seating][maximum])

for x, y in ((-3,4), (5,12), (28, -45)):
    print(math.hypot(x,y))

#   Named tuple

Sale = collections.namedtuple('Sale', 'productid customerid date quantity price')

sales = []
sales.append(Sale(432, 921, '2008-09-14', 3, 7.99))
sales.append(Sale(419, 874, '2008-09-15', 1, 18.49))
total = 0
for sale in sales:
    total += sale.quantity * sale.price
print('Total ${0:.2f}'.format(total))

Aricraft = collections.namedtuple('Aircraft', 'manufacturer model seating')
Seating = collections.namedtuple('seating', 'minumum maximum')
aircraft = Aricraft('Airbus', 'A320-200', Seating(100,220))
print(aircraft.seating.maximum)
print('{0} {1}'.format(aircraft.manufacturer, aircraft.model))
print('{0.manufacturer} {0.model}'.format(aircraft))
print('{manufacturer} {model}'.format(**aircraft._asdict()))

#   Lists

L = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7]
print(L[0] == L[-6] == -17.5)
print(L[1] == L[-5] == 'kilo')
print(L[1][0] == L[-5][0] == 'k')
print(L[4][2] == L[4][-1] == L[-2][2] == L[-2][-1] == 'echo')
print(L[4][2][1] == L[4][2][-3] == L[-2][-1][1] == L[-2][-1][-3] == 'c')

first, *rest = [9 ,2, -4, 8, 7]
print(first, rest)

first, *mid, last = 'Charles Philip Arthur George Windsor'.split()
print(first, *mid, last)

*directories, executable = '/Usuarios/Jacqueline Carvalho/Desktop/Python/PiP - Complete Intro'.split("/")
print(*directories, executable)

def product(a, b, c):
    return a * b * c

print(product(2, 3, 5))

L = [6, 2, 8]
print(product(*L))

# List methods
'''
    J.append(x)
    J.count(x)
    J.extend(m)
    J += m
    J.index(x, start, end)
    J.insert(i,x)
    J.pop()
    J.pop(i)
    J.remove(x)
    J.reverse()
    J.sort(...)
'''
woods = ['Cedar','Yew','Fir'] # two ways, same result

#woods += ['Kauri','Larch'])
#woods.extend(['Kauri','Larch'])

#woods[2:2] = ['Pine']
#woods.insert(2,'Pine')

#woods[2:4] =[]
#del woods[2:4]

#   List Comprehensions

#   A list comprehension is an expression and a loop with an\
#   optional condition enclosed in brackets where the loop is\
#   used to generate items for the list

leaps = []
for year in range(1900, 1940):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leaps.append(year)
        print(year)

leaps = [y for y in range(1990, 2000)]
print(leaps)

leaps = [y for y in range(1950, 2000) if y % 4 == 0]
print(leaps)

leaps = [y for y in range(1970, 2000)\
        if (y % 4 == 0 and y % 100 !=0)\
        or (y% 400 == 0)]
print(leaps)

codes = []
for sex in 'MF':
    for size in 'SMLX':
        if sex == 'F' and size == 'X':
            continue
        for color in 'BGM':
            codes.append(sex + size + color)

codes = [s + z + c \
        for s in 'MF' \
        for z in 'SMLX' \
        for c in 'BGW' \
            if not (s == 'F' and z == 'X')]
print(codes)

print('-------------------------------------------------- Set Types')

#   Set

print(set('pecan') | set('pie'))
print(set('pecan') & set('pie'))
print(set('pecan') - set('pie'))
print(set('pecan') ^ set('pie'))
'''
if len(sys.argv) == 1 or sys.arg[1] in {'-h', '--help'}:
    for ip in set(ips):
        process_ip(ip)

filenames = set(filenames)
for makefile in {'MAKEFILE','Makefile','makefile'}:
    filenames.discard(makefile)

filenames = set(filenames) - {'MAKEFILE','Makefile','makefile'}
'''
#   Set Comprehensions
'''
html = {x for x in files \
        if x.lower().endswith(('.htm','.html'))}
'''

#   Frozen Sets

print('-------------------------------------------------- Mapping Types')

#   Dictionaries

d1 = dict({"id": 1948, "name": "Washer", "size": 3}) 
d2 = dict(id=1948, name="Washer", size=3) 
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)]) 
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3))) 
d5 = {"id": 1948, "name": "Washer", "size": 3}
d = {"root": 18, "blue": [75, "R", 2], 21: "venus", -14: None, "mars": "rover", (4, 11): 18, 0: 45}

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d)

print('--- option 1')
for item in d.items():
    print(item[0], item[1])
    print('*')

print('--- option 2')
for key, value in d.items():
    print(key, value)
    print('*')

for value in d.values():
    print(value)
    print('*')

for key in d:
    print(key)
    print('*')

for key in d.keys():
    print(key)
    print('*')

for value in d.values():
    print(value)
    print('*')

for key in d:
    print(key)
    print('*')

for key in d.keys():
    print(key)
    print('*')

d = {}.fromkeys('ABCD', 3)
s = set('ACX')
matches = d.keys() & s
print(matches)

import string
import sys

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word])) 

#   Dictionary Comprehensions

file_sizes = {name: os.path.getsize(name) for name in os.listdir('.')}
file_sizes = {name: os.path.getsize(name) for name in os.listdir('.') if os.path.isfile(name)}

#   Default Dictionaries

words = collections.defaultdict(int)

#   Ordered Dictionaries

d = collections.OrderedDict([('z', -4), ('e', 19), ('k', 7)])
tasks = collections.OrderedDict() 
tasks[8031] = "Backup" 
tasks[4027] = "Scan Email" 
tasks[5733] = "Build System"

print('-------------------------------------------------- Iterating and Copying Collections')


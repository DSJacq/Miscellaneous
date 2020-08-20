import sys
import random

print('-------------------------------------------------- tuple')

tuple = ('One', 'Two')
#print(tuple)
#print(len(tuple))
print(type(tuple))
#print(hash(tuple))

print('-------------------------------------------------- list')
'''
list = ['One', 'Two']
#print(list)
#print(len(list))
print(type(list))
#print(hash(list))
print('-------------------------------------------------- while function')
i = 1
while i < 10:
    print(i)
    i +=1
print('-------------------------------------------------- for loop')
for country in ('Brazil', 'Germany'):
    print(country)
print('-------------------------------------------------- if function')
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if letter in 'AEI0U':
        print(letter, 'is a vowel')
    else:
        print(letter, 'is a consonant')
print('-------------------------------------------------- try | except ')
s = input('enter an integer: ')
try:
    i = int(s)
    print('valid integer entered : ', i)
except ValueError as err:
    print(err)
print('-------------------------------------------------- while function [input]')
print('Type integers, each followed by Enter; or just Enter to finish')
total = 0
count = 0
while True:
    line = input('integer: ')
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count +=1
    else:
        break
if count:
    print('count = ', count, 'total = ', total, 'mean = ', total / count)
print('-------------------------------------------------- while function [Value Error]')
print('Type integers, each followed by Enter; or ^D or ^Z to finish')
total = 0
count = 0
while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
if count:
    print('count = ', count, 'total = ', total, 'mean = ', total/count)
print('-------------------------------------------------- while function [EOFError]')
'''
total = 0
count = 0
while True:
    try:
        line = input()
        if line:
            try:
                number = int(line)
            except ValueError as err:
                print(err)
            total += number
            count += 1
    except EOFError:
        break
if count:
    print('count = ', count, 'total = ', total, 'mean = ', total/count)

print('-------------------------------------------------- while function [int]')
'''
def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)
age = get_int('enter your age: ')
print('-------------------------------------------------- Import packages [sys]')
#import sys
print(sys.argv)
#import random
x = random.randint(1,6)
y = random.choice(['apple', 'banana', 'cherry', 'durian'])
print(x)
print(y)
print('-------------------------------------------------- digits.py')
Zero  = [" *** ", 
         "*   *", 
         "*   *", 
         "*   *",
         "*   *",
         "*   *",
         " *** "]
One   = [" * ",
         "** ",
         " * ",
         " * ",
         " * ",
         " * ",
         "***"]
Two   = [" *** ",
         "*   *",
         "*  * ",
         "  *  ",
         " *   ",
         "*    ",
         "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four  = ["    * ",
         "   ** ",
         "  * * ",
         " *  * ",
         "******",
         "    * ",
         "    * "]
Five  = ["*****",
         "*    ",
         "*    ",
         " *** ",
         "    *",
         "*   *",
         " *** "]
Six   = [" *** ",
         "*   *",
         "*    ",
         "**** ",
         "*   *",
         "*   *",
         " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine  = [" ****",
         "*   *",
         "*   *",
         " ****",
         "    *",
         "    *",
         " *** "]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
def digits(digits):
    try:
        digits = sys.argv[1]
        row = 0
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                line += digit[row] + " "
            print(line)
            row += 1
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, 'in',  digits)
print('-------------------------------------------------- generate_grid.py')
def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print('must be >= ', minimum)
            else:
                return i
        except ValueError as err:
            print(err)
rows = get_int('rows ', 1, None)
columns = get_int('columns: ', 1, None)
minimum = get_int('minimum (or Enter for 0): ', -1000000,0)
default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int('maximum (or Enter for ' + str(default) + '): ', minimum, default)
row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
            line += s
            column += 1
    print(line)
    row += 1
# To generate the grid we use three while loops,\
# the outer one working by rows, \
# the middle one by columns, \
# and the inner one by characters.

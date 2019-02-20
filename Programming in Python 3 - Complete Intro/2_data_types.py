import sys
import math
import cmath
import re
import string

print('-------------------------------------------------- Identifiers and Keywords')
'''
    and
    as
    assert
    break
    class
    continue
    def
    del
    elif
    else
    except 
    False
    finally 
    for 
    from 
    global 
    if 
    import 
    in 
    is
    lambda
    None
    nonlocal
    not
    or
    pass
    raise
    return
    True
    try 
    while 
    with 
    yield 
'''
print('-------------------------------------------------- Integral Types')
'''
#   Numeric Operators and Functions
    x ** y
    x // y
    x % y
    abs(x)
    divmod(x,y)
    pow(x,y)
    pow(x, y, z) # alternative (x** y) % z
    round(x, n)
    bin(i) #binary
    hex(i) #hexadecimal
    int(x)
    int(s, base) # convert string x to an integer
    oct(i) # returns the octal representation of i as a string

#   Integer Bitwise Operators
    or - i | j
    xor - i ^ j
    and - i & j
    shifts left - i << j
    shiffts right - i >> j
    interts - ~ i

#   Booleans
    t = True
    f = False
    t and f
    t and True
'''
print('-------------------------------------------------- Floating-Point Types')

#   Maths Module's Functions and Constants

def equal_float(a,b):
    return abs(a - b) <= sys.float_info.epsilon

#help(sys.float_info)

s = 14.28.hex()
f = float.fromhex(s)
t = f.hex()

#   Complex Numbers

#   Decimal Numbers

print('-------------------------------------------------- Strings')
'''
#   String Escapes
    \ newline
    \ \ 
    \ '
    \ "
    \ a       ASCII BEL
    \ b       ASCII BS
    \ f       ASCII FF
    \ n       ASCII LF
    \ N{name}
    \ ooo
    \ r
    \ t
    \ tttt    16-bit hexadecinal value
    \ Tttt    32-bit hexadecimal value
    \ v       ASCII VT
    \ xh      8-bit hexadecimal value
'''

t = "This is not the best way to join two long strings " + \
    "together since it relies on ugly newline escaping"
s = ("This is the nice way to join two long strings " 
    "together; it relies on string literal concatenation.")
euros = "\N{euro sign} \u20Ac \U000020AC"
i = 'test ' + chr(8734) + chr(0x23B7)

print(t)
print(s)
print(euros)
print(i)

'''
#   Comparing String
    <
    <=
    ==
    !=
    >
    >=
'''
#   Slicing and Striding Strings

s = 'Testing this string here'
t = s[:12]
w = s[::5]
g = s[:2:-2]
r = s[::-1]

print(t)
print(w)
print(g)
print(r)

#   String Operators and Methods

treatises = ['Arithmetica','Conics','Elements']
join = " ".join(treatises)
print(join)
s = ' x ' * 5
print(s)

#   Example 

# Option 1
def extract_from_tag_0(tag, line):
    opener = '<' + tag + '>'
    closer = '</' + tag + '>'
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None

# Option 2
def extract_from_tag_1(tag, line):
    opener = '<' + tag + '>'
    closer = '</' + tag + '>'
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:j]
    return None

#   Example split

s = "/usr/local/bin/firefox"

# Option 1
result = s.rpartition("/") # separeta last occurency
print(result)

# Otpion 2
i = s.rfind("/")
if i == -1:
    result = "", "", s
    print(result)
else:
    result = s[:i], s[i], s[i + 1:]
    print(result)

s = '\t no parking'
strip = s.lstrip(), s.rstrip(), s.strip()
print(strip)

#   Example Split

record = 'Leo Tolstoy * 1828-8-28 * 1910-11-20'

fields = record.split('*')
print(fields)

born = fields[1].split('-')
print(born)

died = fields[2].split('-')
print(died)

print("Leo Tolstoy lived about", int(died[0]) - int(born[0]), "years")

#   Example translate

table = "".maketrans("\N{bengali digit zero}" "\N{bengali digit one}\N{bengali digit two}" "\N{bengali digit three}\N{bengali digit four}" "\N{bengali digit five}\N{bengali digit six}" "\N{bengali digit seven}\N{bengali digit eight}" "\N{bengali digit nine}", "0123456789")
print("\N{bengali digit one}00\N{bengali digit nine}" "\N{bengali digit five}".translate(table))

#   String formatting with str.format() method

print("The novel '{0}' was published in {1}".format('Hard Times', 1854))

#   Field Names

print("{who} turned {age} this year".format(who='She', age=29))

stock = ['paper', 'envelops', 'notepads', 'pens', 'paper clips']
print("We have {0[1]} and {0[2]} in stock".format(stock))

d = dict(animal = 'elephant', weight = 12000)
print("The {0[animal]} weighs {0[weight]} kg".format(d))

print('{}{}{}'.format('Python ', 'can ', 'count.'))

element = 'Silver'
number = 47
print('Element {number} is {element}'.format(**locals()))

print('The {animal} weighs {weight} kg'.format(**d))

#   Conversions

#   Format specifications
'''
    fill
    align
    sign
    #
    0
    width
    ,
    .precision
    type
'''
'''
s = 'The sword of truth'
print('{0:25}'.format(s))
print('{0:>25}'.format(s))
print('{0:^25}'.format(s))
print('{0:-^25}'.format(s))
print('{0:<25}'.format(s))
print('{0:.10}'.format(s))
maxwidth = 12
print('{0}'.format(s[:maxwidth]))
print('{0:.{1}}'.format(s, maxwidth))
'''

#   Example print_unicode.py

#   Character Encodings

print('-------------------------------------------------- Examples')

#    quadratic.py

#import cmath
#import math
#import sys

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('zero is not allowed')
                x = None
        except ValueError as err:
            print(err)
    return x

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0") 
a = get_float("enter a: ", False) 
b = get_float("enter b: ", True) 
c = get_float("enter c: ", True)

#   csv2html.py

def main(): 
    maxwidth = 100 
    print_start() 
    count = 0 
    while True: 
        try: 
            line = input() 
            if count == 0: 
                color = "lightgreen" 
            elif count % 2: 
                color = "white" 
            else: 
                color = "lightyellow"
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()


def print_start(): 
    print("<table border='1'>")

def print_line(line, color, maxwidth): 
    print("<tr bgcolor='{0}'>".format(color)) 
    fields = extract_fields(line) 
    for field in fields: 
        if not field: 
            print("<td></td>") 
        else: 
            number = field.replace(",", "") 
            try: 
                x = float(number) 
                print("<td align='right'>{0:d}</td>".format(round(x))) 
            except ValueError: 
                field = field.title() 
                field = field.replace(" And ", " and ") 
                if len(field) <= maxwidth: 
                    field = escape_html(field) 
                else: field = "{0} ...".format( escape_html(field[:maxwidth])) 
                print("<td>{0}</td>".format(field)) 
                print("</tr>")

def extract_fields(line): 
    fields = [] 
    field = "" 
    quote = None 
    for c in line: 
        if c in "\"'": 
            if quote is None:
                quote = c 
            elif quote == c: 
                quote = None 
            else: 
                field += c 
                continue 
        if quote is None and c == ",": 
            fields.append(field) 
            field = "" 
        else: 
            field += c 
    if field: 
        fields.append(field) 
        return fields 

def escape_html(text): 
    text = text.replace("&", "&amp;") 
    text = text.replace("<", "&lt;") 
    text = text.replace(">", "&gt;") 
    return text

def print_end(): 
    print("</table>")


from collections import namedtuple

# exemple 1
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)

# exemple 2
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print(xyz)
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz.Class)

# Case
import collections, statistics
print('%.2f' % statistics.mean(next((int(student(*row).MARKS) 
        for row in (input().split() 
                    for i in range(size))) 
                                    for size, 
        student in [[int(input()), collections.namedtuple('Student', input())]])))

# input
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7 
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6 

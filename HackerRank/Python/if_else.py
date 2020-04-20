#!/bin/python3


N = int(input())

# option 1
if (N in range (1, 100) and N % 2 != 0):
    print("Weird")
elif (N in range (2, 6) or N % 2):
    print("Not Weird")
elif (N in range (6,21) or N % 2):
    print('Weird')
else:
    print('Not Weird')

# option 2
if (n %2) == 0 and n in range(6,20) or (n %2) != 0:
    print("Weird")
else:
    print("Not Weird")

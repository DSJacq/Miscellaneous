# list

a = raw_input()
# 5 4 3 2
lis = a.split()
print(lis)
# ['5', '4', '3', '2']

newlis = list(map(int, lis))
print(newlis)
# [5, 4, 3, 2]


# sets

myset = {1, 2} # Directly assigning values to a set
myset = set()  # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
myset
# {'a', 'b'}


# modify sets

myset.add('c')
myset
# {'a', 'c', 'b'}
myset.add('a') # As 'a' already exists in the set, nothing happens
myset.add((5, 4))
myset
# {'a', 'c', 'b', (5, 4)}

myset.update([1, 2, 3, 4]) # update() only works for iterable objects
myset
# {'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
myset.update({1, 7, 8})
myset
# {'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
myset.update({1, 6}, [5, 13])
myset
# {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}


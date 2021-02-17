import itertools

print(list(itertools.product([1,2,3],repeat = 2)))
print(list(itertools.product([1,2],[3,4])))

A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

print(*itertools.product(A, B))

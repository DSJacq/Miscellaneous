from itertools import combinations_with_replacement as combinations
s,n = input().split()
print(*[''.join(p) for p in combinations(sorted(s), int(n))], sep='\n')

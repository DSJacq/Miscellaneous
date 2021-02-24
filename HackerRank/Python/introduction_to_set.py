print(set('HackerRank'))
print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))
print(set({'Hacker' : 'DOSHI', 'Rank' : 616 }))
print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

try:
    print(1/0)
except ZeroDivisionError as e:
    print("Error Code:",e)
    
for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
        
# input
# 3
# 1 0
# 2 $
# 3 1

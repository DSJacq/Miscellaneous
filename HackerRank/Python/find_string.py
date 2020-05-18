# Option 1

def count_substring(string, sub_string):
    return len([i for i in range(len(string)) if string[i:i+len(sub_string)]==sub_string])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
# Option 2
    
    A = raw_input().strip()
x = raw_input().strip()

count = 0
for i in range(len(A) - len(x) + 1):
    if A[i:i+len(x)] == x:
        count += 1
print count

# Option 3

import re
a = raw_input()
b = raw_input()
match = re.findall('(?='+b+')',a)
print len(match)


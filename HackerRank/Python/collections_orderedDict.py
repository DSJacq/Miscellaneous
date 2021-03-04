from collections import OrderedDict

ordinary_dictionary = {}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5

ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5

dct = OrderedDict()
for _ in range(int(input())):
    i = input().rpartition(" ")
    dct[i[0]] = int(i[-1]) + dct[i[0]] if i[0] in dct else int(i[-1])
for l in dct:
    print(l, dct[l])
    
# input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

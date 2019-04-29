# DEFAULT DICT

from collections import defaultdict

# usage of defaultdic objects

def main():
    # define a list to count
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)
    # fruitCounter = defaultdict(lambda: 100)

    # count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # pritn the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
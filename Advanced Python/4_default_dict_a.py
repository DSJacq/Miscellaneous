# DEFAULT DICT

# usage of defaultdic objects

def main():
    # define a list to count
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = {}

    # count the elements on conventional way
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1


    # pritn the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
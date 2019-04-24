# UTILITIES

def main_utilities():
    # Use any() and all() to test sequeces for boolean values
    list_1 = [1, 2, 3, 0, 5, 6]

    # any will return true if any of the sequences values are true
    print(any(list_1))

    # all will return true only if all values are true
    print(all(list_1))

    # min an max will return minimum and maximum values in a sequence
    print("min: ", min(list_1))
    print("max: ", max(list_1))
    
    # use sum() to sum up all the values in a sequence
    print("sum: ", sum(list_1))

if __name__ == "__main__":
    print("_________ Utilities")
    main_utilities()

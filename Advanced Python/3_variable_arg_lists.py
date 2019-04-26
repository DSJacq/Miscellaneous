# VARIABLES ARGUMENTS LISTS


# use of variables argument lists

# define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # pass different arguments
    print(addition(5, 10, 28))
    print(addition(1, 2, 3))

    # pass an existing list
    myNums = [5, 10, 20, 15]
    print(addition(*myNums))


if __name__ == "__main__":
    main()
# KEYWORD-ONLY ARGUMENTS

def myFunction(arg1, arg2, *, suppressExceptions=False):
    pass


def main():
    # call functin without the keyword
    myFunction(1, 2, suppressExceptions=True)

if __name__ == "__main__":
    main()

    
# FUNCTION DOCUMENTATION STRING

# Use of functions doctrings PEP 257

def myFunction(arg1, arg2=None):
    """
    Parameters:
    arg1: The first argument.
    arg2: The second argument.
    """
    print(arg1, arg2)

def main():
    print(myFunction.__doc__)

if __name__ == "__main__":
    main()

# LAMBDA FUNCTIONS

# use lambdas as in-place functions


def CelsiusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahreinheitToCelcius(temp):
    return(temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # use regular functions to convert temps
    print("_____ Regular Function")
    print(list(map(FahreinheitToCelcius, ftemps)))
    print(list(map(CelsiusToFahrenheit, ctemps)))

    # use lambdas to convert temps
    print("_____ Lambda Function")
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))



if __name__ == "__main__":
    main()
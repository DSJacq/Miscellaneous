# ITERATORS

# Use iterator functions like enumerate, zip, iter, next

def main_iterator():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fru", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
        
    # iterate using a function and a sentinel
    # with open("testfile.txt", "r") as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)

    # use regular iteration over the days
    # for m in range(len(days)):
    #     print(m + 1, days[m])

    # using enumerate reduces code and provides a counter
    # for i, m in enumerate(days, start=1):
    #     print(i, m)

    # use zip to combine sequences
    for i,m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "inFrench")


if __name__ == "__main__":
    print('_________ Iterators')
    main_iterator()

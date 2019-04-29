# COUTNER

# usage of counter objects

from collections import Counter

def main():
    # list of students in class 1
    class1 = ['Bob', 'Becky', 'Darcy', 'Frank', 'Hannah', 'Kevin', 'James', 'James', 'Melanie', 'Penny', 'Steve']

    # list of students in class 2
    class2 = ['Bill', 'Barry0', 'Cindy', 'Debbie', 'Frank', 'Gabby', 'Kelly', 'James', 'Joe', 'Sam', 'Tara', 'Ziggy']

    # create a coutner for class 1 and class 2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # how many students in class 1 names James?
    print(c1['James'])

    # how many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "students in class noth classes")

    # what is the most common name in the two classes?
    print(c1.most_common(3))

    # separate the classes agian
    c1.subtract(class2)
    print(c1.most_common(3))

    # what is common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()
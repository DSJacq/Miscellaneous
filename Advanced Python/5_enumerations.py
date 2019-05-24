# DEFINING ENUMERATIONS

from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

def main():
    pass

    # enumerators have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enumerators have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enumerators are hashabela, hence can be used as keys
    myFruit = {}
    myFruit[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruit[Fruit.BANANA])

if __name__ == "__main__":
    main()

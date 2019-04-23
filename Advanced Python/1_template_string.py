# SET UP
from string import Template


# TEMPLATE STRINGS


def main():
    # Usual string formatting with format()
    str1 = "Tesgint my {0} by {1}".format("Algorithm","Jacque Carvalho")
    print(str1)

    # use substitute method with keyword arguments
    templ = Template("Testing my ${word_1} by ${word_2}")

    # use the substitute method with keyword arguments
    str2 = templ.substitute(word_1="Algorithm", word_2="Jacque Carvalho")
    print(str2)

    # use substitute method with dictionary
    data = {
        "word_1" : "Algorithm",
        "word_2" : "Jacque Carvalho"
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == "__main__":
    main()


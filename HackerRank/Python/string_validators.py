if __name__ == '__main__':
    s = raw_input()
    print any([char.isalnum() for char in s]) # string are alphanumeric (a-z, A-Z and 0-9)
    print any([char.isalpha() for char in s]) # string are alphabetical (a-z and A-Z)
    print any([char.isdigit() for char in s]) # string are digits (0-9)
    print any([char.islower() for char in s]) # string are lowercase characters (a-z)
    print any([char.isupper() for char in s]) # string are uppercase characters (A-Z)

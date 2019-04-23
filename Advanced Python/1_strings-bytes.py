# STRINGS VS BYTES

# Strings and byte are not directly interchangeable
# Strings contain unicode, bytes are raw 8-bit values

def main_1():
    # Define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # Try to combine them:
    # print(s + b) # TypeError: can only concatenate str (not "bytes") to str

    # Bytes and srtrings need to be properly encoded and decoded before you can work with them together
    s2 = b.decode('utf-8')
    print(s+s2)

    b2 = s.encode('utf-8')
    print(b+b2)

    # encode de string as UTF-32
    b3 = s.encode('utf-32')
    print(b3)


if __name__ == "__main__":
    main_1()

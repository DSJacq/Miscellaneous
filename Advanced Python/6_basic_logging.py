# BASIC LOGGING

import logging

def main():

    # use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
    filename="output.log",
    filemode="w")

    # try each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    # output formatted strings to the log
    logging.info("Here is a {} variable and an int:".format("string",10))

if __name__ == "__main__":
    main()


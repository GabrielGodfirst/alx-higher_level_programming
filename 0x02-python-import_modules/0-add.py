#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    # Import the add function from add_0.py
    exec(open("add_0.py").read())

    # Use the add function and print the result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))

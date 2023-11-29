#!/usr/bin/python3

# Use a loop to iterate over numbers from 0 to 99
for number in range(100):
    print("{:02d}".format(number), end=", " if number < 99 else "\n")

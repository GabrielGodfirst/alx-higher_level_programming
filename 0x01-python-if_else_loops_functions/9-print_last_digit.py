#!/usr/bin/env python3

def print_last_digit(number):

    last_digit = number % 10
    print("{:04d}".format(last_digit))
    return "{:04d}".format(last_digit)


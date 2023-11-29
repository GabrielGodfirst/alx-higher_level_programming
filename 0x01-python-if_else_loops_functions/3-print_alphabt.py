#!/usr/bin/python3

for ascii_value in range(ord('a'), ord('z') + 1):
    # Check if the character is 'q' or 'e'; if not, print it without a newline
    if chr(ascii_value) not in ('q', 'e'):
        print(chr(ascii_value), end='')

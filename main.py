# this project asks user to enter an integer length, generates a random string with specified length
# and copies it to clipboard test

from random import choice
from string import ascii_lowercase
import pyperclip
import os.path
import sys

# create the folder
folder = os.path.expanduser("~\\Desktop\\String Generator\\")
if not os.path.exists(folder):
    os.makedirs(folder)

while True:
    # loop until user enters 0
    while True:
        # loop until user enters valid length
        try:
            length = int(input("\nEnter valid string length or 0 to exit: "))
        except ValueError as e:
            print("ERROR: " + str(e))
            continue
        if length == 0:
            sys.exit(0)
        elif length > 0:
            break

    new_str = ''.join(choice(ascii_lowercase) for s in range(length))
    if length > 15:
        # if length > 15 - long enough to apply prefix and suffix
        prefix = str(length) + '_chars_'
        suffix = '_end'
        final_str = prefix + new_str[len(prefix):len(new_str) - len(suffix)] + suffix
    else:
        if length > 2:
            # if length > 2 - long enough just for underscore delimiter
            prefix = str(length) + '_'
            final_str = prefix + new_str[len(str(prefix)):]
        else:
            final_str = new_str

    # test that result string has correct length
    try:
        assert len(final_str) == length, "\nERROR: generated string doesn't match specified length"
        print('\n' + final_str + '\n')
        pyperclip.copy(final_str)  # copy to clipboard

        # write to a file
        filename = 'generated strings.txt'
        path = os.path.join(folder, filename)
        with open(path, 'a') as file:
            file.write(final_str + '\n\n')
    except AssertionError as e:
        print(e)






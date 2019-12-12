"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import sys

def random_string_generator(length=12):
    arg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    empty_str = ''
    while count < length:
        empty_str += random.choice(arg)
        count += 1
    return empty_str

def batch_string_generator(num_rand_str, min_str_len=8, max_str_len=12):
    ls = []
    for i in range(num_rand_str):
        if min_str_len < max_str_len:
            rand_result = random.choice(range(min_str_len, max_str_len))
        elif min_str_len == max_str_len:
            rand_result = min_str_len
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        ls.append(random_string_generator(rand_result))
    return ls

min_str_len = int(input('Enter minimum string length: '))
max_str_len = int(input('Enter maximum string length: '))
num_rand_str = int(input('How many random strings to generate? '))

print(batch_string_generator(num_rand_str, min_str_len, max_str_len))

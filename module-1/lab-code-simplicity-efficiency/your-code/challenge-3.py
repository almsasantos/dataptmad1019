"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

# To measure the time of execution in python we can import the library time as seen below:

import time

start = time.time()

def my_function(max_length):
    if max_length > 5:
        possibilities = [(x, y, z) for x in range(5, max_length) for y in range(4, max_length) for z in range(3, max_length) if (x * x == y * y + z * z)]
        m = 0
        for solution in possibilities:
            if m < max(solution):
                m = max(solution)
        return m
    else:
        return 'impossible to calculate, maximal length should be greater than 5!'

max_length = int(input('What is the maximal length of the triangle side? Enter a number: '))
print(f'The longest side possible is {my_function(max_length)}')

end = time.time()

print(f'The total time of execution of this function was {end - start}')

#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random([2, 3, 5])
a = np.random.rand(2, 3, 5)

#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5, 2, 3))


#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
print(f'The size of array a is {a.size} and the size of array b is {b.size}', end='')
if a.size == b.size:
    print(', a and b are the same size')
else:
    print(', a and b are not the same size')


#8. Are you able to add a and b? Why or why not?

#If I execute the following command print(a+b) I'll get a ValueError because the arrays a and b have different shapes.
#To see the shape of each array you can execute the following two commands: print(a.shape) print(b.shape)
try:
    print(a+b)
except ValueError:
    print("It's not possible to add arrays of different shapes.")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable "c".
#c = np.reshape(2, 3, 5)
c = b.transpose(1,2,0)
print(c.shape)


#10. Try to add a and c. Now it should work. Assign the sum to variable "d". But why does it work now?
#There are two ways of adding a and c. First one is using the mathematical plus operator and other one is using a function built in numpy called add().
d = np.add(a, c)
d = a + c


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)


# If we subtract the array d to a we'll get an array of ones. Both have the same shape and size.
print(d - a)


#12. Multiply a and c. Assign the result to e.
# Again there're two ways in code to write this multiplication.
e = a * c
e = np.multiply(a, c)


#13. Does e equal to a? Why or why not?
print(np.array_equal(e, a))
# Using the command above we'll get a boolean value, returns True if both arrays are equal and False if they're different.
# Both arrays are equal because the array e came from the multiplication of array a and c.
# Since array c came from the reshape of array b, and array b was an array full of ones.
# The result of multiplying an array full of different numbers for an array full of ones, the first array will always be equal to that one.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(f'In array d the maximum value is {d_max}, the minimum value is {d_min} and the mean equals to {d_mean}')


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5))

print('Done with exercise 15.')
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.

f1 = [[[25 if d_min<elem3<d_mean else 75 if d_mean<elem3< d_max else 0 if elem3 == d_min else 100 for elem3 in elem2] for elem2 in elem1] for elem1 in d]
print(f1)

f = np.array(f1)

'''
I tried to do this same exercise using numpy built-in functions but I couldn't get the full changed array, just value by value.
I'll leave it below, because I think it'll be interesting for me in the future to come back and find it's solution.
np.where((d > d_min) & (d < d_mean), 25, d)
np.where((d > d_mean) & (d < d_max), 75, d)
np.where(d == d_mean, 50, d)
np.where(d == d_min, 0, d)
f = np.where((d == d_max), 100, d)
print(f)'''


#17. Print d and f. Do you have your expected f?
#For instance, if your d is:
'''array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

#Your f should be:
f_array = array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])'''
print(d)
print(f)


#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
#("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
'''array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])'''
#Again, you don't need Numpy in this question.
f2 = [[['A' if elem3 == 0 else 'B' if elem3 == 25 else 'E' if elem3 == 100 else 'D' for elem3 in elem2] for elem2 in elem1] for elem1 in f1]
print(f'The following list helps us to create the correct array: {f2}')
new_f_array = np.array(f2)
print('This is new array full of strings:')
print(new_f_array)


#PEDRO EXERCISE:
# Why writing this command sum(d[:0]) will return the same result as np.sum(d[:0])
# In my opinion both options work because sum is a built-in function of python, so if we pass an argument to that function it'll execute it.
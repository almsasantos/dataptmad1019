import os
from os.path import join, isfile
import numpy as np
import pandas as pd

#1. Use a list comprehension to create and print a list of consecutive integers starting with 1 and ending with 50.
lst1 = [i for i in range(1, 51)]
print(lst1)

#​2. Use a list comprehension to create and print a list of even numbers starting with 2 and ending with 200.
lst2 = [i for i in range(2, 201) if i%2==0]
print(lst2)

'''lst2 = []
for i in range(2, 201):
    if i%2 == 0:
        lst2.append(i)
print(lst2)'''

#3. Use a list comprehension to create and print a list containing all elements of the 10 x 4 Numpy array below.
a = np.array([[0.84062117, 0.48006452, 0.7876326 , 0.77109654],
       [0.44409793, 0.09014516, 0.81835917, 0.87645456],
       [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
       [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
       [0.17003563, 0.46843998, 0.92796258, 0.69814654],
       [0.41290051, 0.19561071, 0.16284783, 0.97016248],
       [0.71725408, 0.87702738, 0.31244595, 0.76615487],
       [0.20754036, 0.57871812, 0.07214068, 0.40356048],
       [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
       [0.80930099, 0.50962849, 0.94555126, 0.33364763]])

#list_a1[row for row in a for cell in row]
list_a1 = [cell for row in a for cell in row]

print(list_a1)

#4. Add a condition to the list comprehension above so that only values greater than or equal to 0.5 are printed.
list_a2 = [cell for row in a for cell in row if cell >= 0.5]

print(list_a2)

#5. Use a list comprehension to create and print a list containing all elements of the 5 x 2 x 3 Numpy array below.
b = np.array([[[0.55867166, 0.06210792, 0.08147297],
               [0.82579068, 0.91512478, 0.06833034]],

              [[0.05440634, 0.65857693, 0.30296619],
               [0.06769833, 0.96031863, 0.51293743]],

              [[0.09143215, 0.71893382, 0.45850679],
               [0.58256464, 0.59005654, 0.56266457]],

              [[0.71600294, 0.87392666, 0.11434044],
               [0.8694668, 0.65669313, 0.10708681]],

              [[0.07529684, 0.46470767, 0.47984544],
               [0.65368638, 0.14901286, 0.23760688]]])

list_b1 = [sub_sub_element for element in b for sub_element in element for sub_sub_element in sub_element]

print(list_b1)

#5. Add a condition to the list comprehension above so that the last value in each subarray is printed, but only if it is less than or equal to 0.
list_b2 = [sub_element for element in b for sub_element in element for sub_sub_element in sub_element if sub_sub_element <= 0]

print(list_b2)

#6. Use a list comprehension to select and print the names of all CSV files in the /data directory.
mypath = '/home/almsasantos/Desktop/Ironhack/dataptmad1019/module-1/lab-list-comprehensions/data/'

onlyfiles = [file for file in os.listdir(mypath) if file.endswith('.csv')]

print(onlyfiles)

#7. Use a list comprehension and the Pandas read_csv and concat methods to read all CSV files in the /data directory and combine them into a single data frame.
# Display the top 10 rows of the resulting data frame.

import fnmatch
csv_files = fnmatch.filter(os.listdir(mypath), '*sample*.csv')
dfs = [pd.read_csv(mypath + os.sep + csv_file) for csv_file in csv_files]

df = pd.concat(dfs, axis=0)

#To see the resulting data frame
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
       #print(df)
print(df.iloc[0:10])

#8. Use a list comprehension to select and print the column numbers for columns from the data set whose median is less than 0.48.
import fnmatch
csv_files = fnmatch.filter(os.listdir(mypath), '*sample*.csv')
dfs = [pd.read_csv(mypath + os.sep + csv_file) for csv_file in csv_files]

df = pd.concat(dfs, axis=0)

selected_columns = [col for col in df._get_numeric_data() if df[col].median() < 0.48]

print(selected_columns)

#9. Use a list comprehension to add a new column (20) to the data frame whose values are the values in column 19 minus 0.1.
# Display the top 10 rows of the resulting data frame.
#First we need to create a list to convert it into a column:
twenty = [0.123456, 0.654321, 0.123456, 0.654321, 0.123456]

df['20'] = twenty

print(df.iloc[0:10 ])

#10. Use a list comprehension to extract and print all values from the data set that are between 0.7 and 0.75.
import fnmatch
csv_files = fnmatch.filter(os.listdir(mypath), '*sample*.csv')
dfs = [pd.read_csv(mypath + os.sep + csv_file) for csv_file in csv_files]

df = pd.concat(dfs, axis=0)
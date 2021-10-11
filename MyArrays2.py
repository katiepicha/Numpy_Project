import numpy as np

# ROWS - each student (student0, student1, student2, student3)
# COLS - each test (test0, test1, test2)
grades = np.array([[87, 96, 70], [100, 87, 90],
                    [94, 77, 90], [100, 81, 82]])

student1 = grades[1]

student0_test1 = grades[0, 1] # first row, second test ("," helps represent particular columns)

students0_1 = grades[0:2] # ":" for sequential values and upper bound is NOT included

# non-sequential values
students1and3 = grades[[1,3]] # [[]] represents only the row part and allows you to use a comma
# to select students 1 and 3 BUT only test 2
students1and3_test2 = grades[[1,3], 1]

# all the students but only test0
all_students_test0 = grades[:, 0] # just the ":" tells python to get all the rows

# all students, test 1 and 2
all_students_test1_2 = grades[:, 1:3] # consecutive columns do NOT need brackets

# all students, test 0 and 2
all_students_test0and2 = grades[:, [0,2]] # non-consecutive columns (with a "," required) need brackets


''' 
Class Exercise
Use NumPy random-number generation to create an array of twelve random grades in the range 60 through 100, then reshape the
result into a 3-by-4 array. Calculate the average of all the grades, the averages of the grades for each test and the averages
of the grades for each student.
'''

import random

grades1 = np.random.randint(60, 101, 12).reshape(3, 4)
grades1.mean() # average of all grades
grades1.mean(axis = 0) # average by column (each test)
grades1.mean(axis = 1) # average by row (each student)



numbers = np.arange(1,6)

# creating a SHALLOW copy
numbers_view = numbers.view()
# whatever you do to the original, also affects the shallow copy
numbers[1] *= 10
# whatever you do to the shallow copy also affects the original
numbers_view[1] /= 10
# slices also create a shallow copy that is affected by the original
numbers_slice = numbers[0:3]
numbers[1] *= 20

# creating a DEEP copy
numbers_copy = numbers.copy()
# whatever you do to the original does NOT affect the deep copy
numbers[1] *= 10


grades = np.array([[87, 96, 70], [100, 87, 90]])

# reshape method produces a shallow copy
grades_reshaped = grades.reshape(1, 6)

# resize method changes the original array
grades.resize(1, 6)

# flatten creates a deep copy (1 dimensional array)
flattended = grades.flatten()
flattended[1] = 100

# ravel creates a shallow copy
raveled = grades.ravel()
raveled[0] = 100


grades = np.array([[87, 96, 70], [100, 87, 90]])

# transpose - flips rows and columns
grades.T

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

# hstack (horizontal stack) - adds more columns to the rows
h_grades = np.hstack((grades, grades2))

# vstack (vertical stack) - adds more rows to the columns
v_grades = np.vstack((grades, grades2))



print()
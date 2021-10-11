import numpy as np
import random


# two dimensional array (has rows and columns)
# [1,2,3] is the first row with 3 elements and [4,5,6] is the second row with 3 more elements
arr01 = np.array([[1,2,3],
                  [4,5,6]])

# one dimensional array
arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

for row in arr01:
    print(row)
    for col in row:
        print(col, end = ' ')
    print()

# flat disregards elements in rows and just prints each element one at a time
for i in arr01.flat:
    print(i)


arr03 = np.zeros(5)

arr04 = np.ones((2, 4), dtype = int)

arr05 = np.full((3, 5), 13)


# ------------------------- EXERCISE ------------------------------

# create a 2 dimensional array of 5 integer elements each using the random module and list comprehension

a = np.array([[random.randint(1,10) for n in range(5)], 
                  [random.randint(1,10) for n in range(5)]])
print(a)


b = np.array(np.random.randint(1, 10, size = (2, 5)))
print(b)

# ----------------------------------------------------------------
# range function in numpy is known as arange()

# start at 0, end at 5 (not included)
arr06 = np.arange(5)

# 5 is start value, but 10 is end value (not included)
arr07 = np.arange(5,10)

# start at 10, end at 1 (not included) and goes down by 2
arr08 = np.arange(10, 1, -2)

# ----------------------------------------------------------------

# linspace() allows you to create an array of numbers that are equally spaced out
# starting number and end number ARE included
arr09 = np.linspace(0.0, 1.0, num = 5)

# reshape must be a factor/multiple of the number
arr10 = np.arange(1, 21).reshape(4, 5)


# broadcasting - takes a scalar value and expands it to match the number of elements in the original array
# broadcasting does not affect the original array

num01 = np.arange(1, 6)

num02 = num01 * 2 # multiplies the number two with every element in num01

num03 = num01 ** 3

# augmented assignment changes the original array
num01 += 10

num04 = num01 * num02 # arrays must be the same size/length

# will return True or False if it meets criteria
num05 = num01 > 13

num06 = num03 > num01


# Here we have an array of 4 students grades on 3 exams
# row = student
# col = exam
grades = np.array([[87, 96, 70], [100, 87, 90],
                    [94, 77, 90], [100, 81, 82]])

# summaries/aggregate functions across the board - NOT for a particular student
print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

# calculate average on all rows for each column (specific for exam)
grades_by_exam = grades.mean(axis = 0) # will produce a 1 dimensional array with 3 elements (averages for each exam)

# calculate average on all columns for each row (specific for student)
grades_by_student = grades.mean(axis = 1) # will produce a 1 dimensional array with 4 elements (averages for each student)


# universal functions in Numpy

# square root
num07 = np.array([1, 4, 9, 16, 25, 36])
num08 = np.sqrt(num07)

# add (same as concatenation)
num09 = np.array([10, 20, 30, 40, 50, 60])
num10 = np.add(num07, num09)
# same as
num10 = num07 + num09

# multiply
num11 = np.multiply(num09, 5)
# same as
num11 = num09 * 5

# number of rows do NOT have to match up, but the number of columns do
num12 = num09.reshape(2,3)
num13 = np.array([2, 4, 6])
num14 = np.multiply(num12, num13)


print()
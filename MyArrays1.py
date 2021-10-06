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

# start at 0, end at 5 (not included)
arr06 = np.arange(5)

# 5 is start value, but 10 is end value (not included)
arr07 = np.arange(5,10)

# start at 10, end at 1 (not included) and goes down by 2
arr08 = np.arange(10, 1, -2)



print()
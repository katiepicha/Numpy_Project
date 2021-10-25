## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
total_sales = salesArray.sum()
print(total_sales)

print()

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
smallest_sale = salesArray.min()
largest_sale = salesArray.max()
print('Smallest sale:', smallest_sale)
print('Largest sale:', largest_sale)

print()

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")
sales100 = salesArray >= 100
print(sales100)

print()

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
sales_by_register = salesArray.sum(axis = 1)
print(sales_by_register)

print()

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")
sales_fee = salesArray * 0.02
sales_fee_rounded = np.round_(sales_fee, decimals=2)
total_fee = sales_fee_rounded.sum()
total_fee_rounded = np.round_(total_fee, decimals=2)
print(sales_fee_rounded)
print()
print('Total Fees:', total_fee_rounded)

print()

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")

print()

## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")
cash_register2_and4 = salesArray[[1,3]]
print(cash_register2_and4)

print()

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])
salesArray2 = np.vstack((salesArray, newRegister))
print(salesArray2)

print()

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")
print('Before:')
print(salesArray2)
salesArray2[2,3] = 20.14
print('After:')
print(salesArray2)
print()


# Exercises: Day 10

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.

'''
#using for loop
for i in range(0,11):
    print(i)
    
'''
'''
#using while loop
i=0
while(i<=10):
    print(i)
    i=i+1

'''
    
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
'''
#using while loop
i = 10
while (i>=0):
    print(i)
    i=i-1
'''
'''
#using for loop
for i in range(10,-1,-1):
    print(i)

'''    

# 3.Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
'''

for i in range(1,8):
    for j in range(1,i+1):
        print('#', end="")
    print("\r")
'''
# 4. Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

'''
for i in range(1,9):
    for j in range(1,9):
        print('#', end="")
    print("\r")
'''
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

'''
for i in range(0,11):
       print(f'{i} X {i} = {i*i}')
'''
   
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
'''
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for litem in list:
    print(litem)
'''
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
'''
for i in range(0,101):
    if i%2 == 0:
        print(i)
'''
        
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
'''
for i in range(0,101,):
    if i%2 != 0:
        print(i)
'''


# Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
'''
sum = 0
for i in range(0,101):
    sum = sum + i
print("The sum of all numbers is ",sum)
'''

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.

'''
sum_even = 0
sum_odd = 0
for i in range(0,101):
    if i%2 ==0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
print(f' The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}')
'''


# Exercises: Level 3

# 1. Go to the data folder and use the countries_data.py file. Loop through the countries and extract all the countries containing the word land.
import sys
sys.path.append('data')

import countries_data

list_c = countries_data.countries

'''
for country in list_c:
    if 'land' in country:
        print(country)
'''
        
# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon'] 
'''
rev = []
for i in range(3,-1,-1):
    rev.append(fruit_list[i])
print("Reversed list: ",rev)


'''
# 3. Go to the data folder and use the countries.py file.
# i. What are the total number of languages in the data
# ii.Find the ten most spoken languages from the data
# iii.Find the 10 most populated countries in the world

## --- Note --- Unsolved ------
#Exercises: Level 1

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# 3. Declare a first name variable and assign a value to it
import math


first_name = "Anju"

# 4. Declare a last name variable and assign a value to it
last_name = "Soren"

# 5. Declare a full name variable and assign a value to it
full_name = "Anju Soren"

# 6. Declare a country variable and assign a value to it
country = "India"

# 7. Declare a city variable and assign a value to it
city = 'Raipur'

# 8. Declare an age variable and assign a value to it
age = 26

# 9. Declare a year variable and assign a value to it
year = 2023

# 10. Declare a variable is_married and assign a value to it
is_married = False

# 11. Declare a variable is_true and assign a value to it
is_true = True

# 12. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 13. Declare multiple variable on one line
a,b = 12,29




# Exercises: Level 2

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))

# 3. Compare the length of your first name and your last name
print(len(last_name))  #last_name is of greater length

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# i. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

# ii. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)

# iii. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

# iv. Divide num_one by num_two and assign the value to a variable division
divison = num_one / num_two
print(divison)

# v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
modulus = num_two % num_one
print(modulus)

# vi. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

# vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = math.floor(num_one / num_two)
print(floor_division)

# 5. The radius of a circle is 30 meters.
radius = 30

# i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * radius * radius
print(area_of_circle)

# ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

# iii. Take radius as user input and calculate the area.
r = input("enter the radius : ")
area = math.pi * int(r) * int(r)
print(area)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
fname = input("Enter your first name : ")
lname = input("Enter your last name : ")
country1 = input("Enter your country : ")
age1 = input("Enter your age : ")

print("Your first name is ", fname)
print("Your last name is ", lname)
print("Your country is ",country1)
print("Your age is ",age1)

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help(True))
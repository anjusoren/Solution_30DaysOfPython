# Exercises - Day 3

# 1.Declare your age as integer variable
import math


age = 26

# 2. Declare your height as a float variable
height = 150.0

# 3. Declare a variable that store a complex number
comp_num = 1 + 2j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

'''
b = input("Enter base : ")
h = input("Enter height : ")
area = 0.5 * int(b) * int(h)
print("The area of the triangle is ", int(area))
'''

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

'''
a = input("Enter side a: ")
b = input("Enter side b: ")
c = input("Enter side c: ")
perimeter = int(a) + int(b) + int(c)
print("The perimeter of the triangle is ", perimeter)
'''

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
'''
length = int(input("Enter length : "))
width = int(input("Enter width : "))
area = length * width
perimeter  = 2 * (length + width)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)
'''

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
r = int(input("Enter the radius of circle : "))
area = math.pi * r * r
perimeter  = 2 * math.pi * r
print("The area of the circle : ",area)
print("The perimeter of the circle is ", perimeter)
'''
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
'''
x = int(input("Enter the value of x : "))
y = (2 * x) - 2
print("The slope is ",y)
'''

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# 10. Compare the slopes in tasks 8 and 9.
'''
x1, y1 = 2,2
x2, y2 = 6,10

m = (y2 - y1)/(x2 - x1)
print("Euclidean distance : ",m)
'''

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''
x = int(input("Enter the value of x : "))
y = (x ** 2) + (6 *x) + 9
print("The value of y is ",y)
'''

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
'''
print("The length of word python is ",len('python'))
print("The length of word dragon is ", len('dragon'))

'''

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
print("on in python : ",'on' in 'python')
print('on in dragon : ', 'on' in 'dragon')
'''
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# print("I hope this course is not full of jargon. 'jargon' is present in the line : ", 'jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python
# print("dragon and python includes on : ", 'on' in 'dragon' and 'on' in 'python')

# 16 .Find the length of the text python and convert the value to float and convert it to string
'''
length = len('python')
print("Length of python : ",length)
convert_to_float = float(length)
print("Length in float : ",convert_to_float)
convert_to_string = str(convert_to_float)
print("Convert it to string : ",convert_to_string)

'''

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
'''
num = int(input("Enter the number : "))
if(num%2 == 0):
    print(num, " is even number")
else :
    print(num , 'is odd number')
'''

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
'''
floor_div = 7/3
print("floor division of 7 by 3 is ", math.floor(floor_div))
num = 2.7
print("int converted value of 2.7 ",int(num))
'''

# 19. Check if type of '10' is equal to type of 10
''' #equal
print(type('10'))
print(type(10))
'''

# 20. Check if int('9.8') is equal to 10
''' #not equal
num = int('9.8')
print(type(num))
print(type(10))
'''

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
'''
hours = int(input("Enter hours : "))
rate_per_hour = int(input("Enter rate per hour : "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is ", weekly_earning)
'''

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

number_of_years = int(input("Enter the number of years : "))
lived_seconds = number_of_years * 365 * 24 *60 *60
print("You have lived for ",lived_seconds," seconds.")

# 23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

#unsolved
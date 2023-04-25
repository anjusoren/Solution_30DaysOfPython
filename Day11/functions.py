# Exercises: Day 11

# Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
from math import pi, sqrt
import math


def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

# print(add_two_numbers(1,6))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = pi * r * r
    return area

#print(area_of_circle(10))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

#print(add_all_nums(1,2,3,4))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * (9/5))+ 32
    return f

#print(convert_celsius_to_fahrenheit(21))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month == "september" or month == "october" or month == "november":
        return "The season is Autumn."
    elif month == "december" or month == "january" or month == "february":
        return "The season is Winter."
    elif month == "march" or month == "april" or month == "may":
        return "The season is Spring."
    elif month == "june" or month == "july" or month == "august":
        return "The season is Summer."
    else:
        return "Please enter the month name correctly."

#print(check_season("September"))

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1)/(x2 - x1)
    return m

#print(calculate_slope(1,2,3,4))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

'''
[Math- domain error : sqrt]
def solve_quadratic_equation(a, b,c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - math.sqrt(d))/(2 * a)
    sol2 = (-b + math.sqrt(d))/(2 * a)
    return sol1, sol2
    
print(solve_quadratic_equation(8,5,9))
'''
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(a):
    for item in a:
        print(item)

#print_list(['apple','orange','mango','pear'])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]

def reverse_list(a):
    for item in reversed(a):
        print(item)
        
#reverse_list([1, 2, 3, 4, 5])
    
# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(str_list):
    for str_ele in str_list:
        print(str_ele.capitalize())
        
#capitalize_list_items(['sand','spider','marvel','jack'])

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(list_o, ele):
    list_o.append(ele)
    return list_o

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(add_item(food_staff, 'Meat'))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(list_n, ele):
    list_n.remove(ele)
    return list_n

numbers = [2, 3, 7, 9]
#print(remove_item(numbers, 3))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050

def sum_of_numbers(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum + i
    return sum

#print(sum_of_numbers(5))
#print(sum_of_numbers(10))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for i in range(num + 1):
        if(i %2 != 0):
            sum = sum + i
        
    return sum 

print(sum_of_odds(9))


# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(num):
    sum = 0
    for i in range(num+1):
        if i%2 == 0:
            sum = sum + i
    return sum 

print(sum_of_even(9))
            

# Exercises: Level 2

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def evens_and_odds(num):
    sum_of_e = 0
    sum_of_o = 0
    for i in range(num + 1):
        if(i % 2 == 0):
            sum_of_e = sum_of_e + i
        else :
            sum_of_o = sum_of_o + i
    print(f'sum of all evens : {sum_of_e} and sum of all odds : {sum_of_o}')
    
#evens_and_odds(9) 


# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num == 0:
        return 1
    elif num == 1 :
        return 1
    else :
        return num * factorial(num - 1)

#print(factorial(4))

# 2. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def function_is_empty(arg):
    if arg :
        return True
    else :
        return False
    
#print(function_is_empty(0))

# 3. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(dataset):
    return sum(dataset)/len(dataset)
#print(calculate_mean([1,2,3,4,5]))

def calculate_median(dataset):
    n = len(dataset)
    index = n // 2
    if n %2 != 0:
        return sorted(dataset)[index]
    return sum(sorted(dataset)[index - 1 : index + 1]) / 2

#print(calculate_median([3, 5, 1, 4, 2]))
    


# Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)):
            if (num % i) == 0:
                print(num , " is not a prime number.")
                break
            else:
                print(num , " is a prime number.")
                break
    else:
        print(num , " is not a prime number.")
        
is_prime(11)

# 2. Write a functions which checks if all items are unique in the list.
def is_unique(r):
    if len(r) > len(set(r)):
        return False
    return True

#print(is_unique([1,2,4,6,8,2,1,4,10,12,14,12,16,17]))

# 3. Write a function which checks if all the items of the list are of the same data type.
def type_check(lr):
    return all(type(element) == type(lr[0]) for element in lr)

print(type_check([5, 6, 2, 5, 7, 9,]))

# 4. Write a function which check if provided variable is a valid python variable
# 5. Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
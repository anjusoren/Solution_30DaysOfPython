# Exercises: Day 9

# Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

'''
age = int(input("enter your age : "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f'You need {18-age} more years to drive.')

'''
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

'''
my_age = 34
your_age = int(input("Enter your age : "))
diff = your_age - my_age
if diff == 0:
    print("Wa both are of same age.")
elif diff == 1:
    print("You are only 1 years older than me.")
elif diff < 1:
    diff = abs(diff)
    print(f'You are {diff} years younger than me.')
else: 
    print(f'You are {diff} years older than me.')

'''

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

'''
a = int(input("Enter number one : "))
b = int(input("Enter number two : "))
if a > b:
    print(f'{a} is greater than {b}.')
else:
    print(f'{b} is greater than {a}.')

'''


# ### Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

'''
scores = int(input("Enter your scores : "))
if scores >=90 :
    print("Grade : A")
elif scores >=70 :
    print("Grade : B")
elif scores >=60 :
    print("Grade : C")
elif scores >=50 :
    print("Grade : D")
else:
    print("Grade : F")
'''
    
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
'''
month = input("Enter the month : ")
month = month.lower()
if month == "september" or month == "october" or month == "november":
    print("The season is Autumn.")
elif month == "december" or month == "january" or month == "february":
    print("The season is Winter.")
elif month == "march" or month == "april" or month == "may":
    print("The season is Spring.")
elif month == "june" or month == "july" or month == "august":
    print("The season is Summer.")
else:
    print("Please enter the month name correctly.")
'''


# 3. The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

'''
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits_name = input("Enter the fruits name : ")
if fruits_name in fruits:
    print("The fruits already exist in the list.")
else:
    fruits.append(fruits_name)
    print("Modified List : ",fruits)

'''

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
#  * 
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
'''
key = 'skills'
if key in person.keys():
    print("Skill is present in the dictionary.")
    print(person[key])
else:
    print("skills is not present in the dictionary.")

'''
#2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
'''

key = 'skills'
if key in person.keys():
    if "Python" in person['skills']:
        print("Python is present.")
else:
    print("skills is not present in the dictionary.")

'''
#3. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
'''
if person['skills']:
    if ['Javascript','React'] == person['skills']:
        print("Front End Developer.")
    elif [ 'Node', 'Python', 'MongoDB'] == person['skills']:
        print("Full Stack Developer.")
    else:
        print("Title Unknown.")
'''
#4. If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and person['country']== 'Finland':
    print(person['first_name']," ",person['last_name']," lives in ",person['country']," . He is married.",)
else:
    print(person['first_name']," ",person['last_name']," lives in ",person['country']," . He is not married.",)
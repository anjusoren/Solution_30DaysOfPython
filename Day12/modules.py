# Exercises: Day 12

# Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'


import random
import string

def random_user_id():
    user_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    return user_id

#print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    no_of_char = int(input("Enter no of character : "))
    no_of_ids = int(input("Enter no of ids : "))
    for ids in range(no_of_ids):
        user_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(no_of_char)])
        print(user_id)
#user_id_gen_by_user()    

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form

from random import randint
def rgb_color_gen():
    print(f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})')
#rgb_color_gen()

# Exercises: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    colors = []
    for i in range(num_colors):
        color = '#'
        for i in range(6):
            color += random.choice('0123456789abcdef')
        colors.append(color)
    return colors
#print(list_of_hexa_colors(3))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    colors = []
    for i in range(num_colors):
        color = f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'
        colors.append(color)
    return colors

#print(list_of_rgb_colors(2))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(num_colors, format='hex'):
    colors = []
    for i in range(num_colors):
        if format == 'hex':
            color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        elif format == 'rgb':
            color = 'rgb({}, {}, {})'.format(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else :
            raise ValueError('Invalid color format. Choose correctly.')
        colors.append(color)
    return colors

#print(generate_colors(7,'hex'))

# Exercises: Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(newlist):
    shuffled_list = newlist[:]
    random.shuffle(shuffled_list)
    return shuffled_list

#print(shuffle_list([1,2,4,8,9,12]))
# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def randomSeven():
    seven = set()
    while len(seven) < 7:
        seven.add(random.randint(0,9))
    return list(seven)

print(randomSeven())
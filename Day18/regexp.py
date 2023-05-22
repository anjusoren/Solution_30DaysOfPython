# Exercises: Level 1

# 1. What is the most frequent word in the following paragraph?
from collections import Counter
from itertools import count
import re


paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

def word_count(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts

print(word_count(paragraph))
print(max(word_count(paragraph)))

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12

new_points_txt ='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
#reg_pattern = r'[-+]?\d'
#points_found = re.findall(reg_pattern, new_points_txt)

def find_numbers(text):
    reg_pattern = r'[-+]?\d'
    numbers = re.findall(reg_pattern,text)
    return [int(num) for num in numbers]

nums = find_numbers(new_points_txt)
print('numbers found : ',nums)
sorted_nums= sorted(nums)
print("sorted numbers : ",sorted_nums)
total = len(nums)
last_index = total - 1
new_distance = sorted_nums[last_index] - sorted_nums[0]
print("Distance : ",new_distance)
#print(sorted_nums[last_index])
#print(sorted_nums[0])


# Exercises: Level 2

# 1. Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

'''
rule for valid python variable-
1. should not start with digit
2. should not contain space
3. should not contain special characters except _
'''
def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, variable) is not None

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))


# Exercises: Level 3

# 1. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
reg_find = r'[%@^;?!$^&#.,]'
clean_text = re.sub(reg_find,'',sentence)
print(clean_text)
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

def find_most_frequent_words(para, num_words):
    clean_para = re.sub(r'[^\w\s]','', para.lower())
    
    words = clean_para.split()
    word_counts = Counter(words)
    
    most_common_words = word_counts.most_common(num_words)
    
    return most_common_words

num_words=3
most_frequent_words = find_most_frequent_words(clean_text,num_words)
print(most_frequent_words)
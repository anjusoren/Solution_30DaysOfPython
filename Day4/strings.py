# Exercises - Day 4


# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'''
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
space = ' '
string = a + space + b + space + c + space + d
print(string)
'''

# 2 .Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'''
a = 'Coding'
b = 'For'
c = 'All'
space = ' '
string = a + space + b + space + c
print(string)

'''


# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
all_upper = company.upper()
print(all_upper)

# 7. Change all the characters to lowercase letters using lower() method.
all_lower = company.lower()
print(all_lower)

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capitalize_company = company.capitalize()
title_company = company.title()
swapcase_company = company.swapcase()

print('-----------------------------------')
print(capitalize_company)
print(title_company)
print(swapcase_company)


# 9. Cut(slice) out the first word of Coding For All string.
slice_company = company[:6]
print(slice_company)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
str = 'Coding'
find_word = str in company
print(find_word)

# 11. Replace the word coding in the string 'Coding For All' to Python.
replace_word = company.replace('Coding', 'Python')
print(replace_word)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
str1 = 'Python for Everyone'
replace_word = str1.replace('Everyone','All')
print(replace_word)

# 13. Split the string 'Coding For All' using space as the separator (split()) .
comp_strings = company.split(' ')
print(comp_strings)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
string1_split = string1.split(',')
print(string1_split)

# 15. What is the character at index 0 in the string Coding For All.
print(company[0]) #C

# 16. What is the last index of the string Coding For All.
print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.
print(company[10]) #space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
'''
string2 = 'Python For Everyone'
strings_in_string2 = string2.split()
print(strings_in_string2)

for i in strings_in_string2:
    print(i[0])

'''
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
'''
print(company)
splitted_company = company.split(' ')
for i in splitted_company:
    print(i[0])`
'''

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
first_c = company.find('C')
print(first_c)

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
first_f = company.find('F')
print(first_f)

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_l = company.rfind('l')
print(last_l)

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
find_because = sentence.find('because')
print(find_because)

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
find_becausel = sentence.rfind('because')
print(find_becausel)

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sen = 'You cannot end a sentence with because because because is a conjunction'
slice1 = sen.split('because because because')
print(slice1)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occur = sen.find('because')
print(first_occur)

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_occur = sen.rfind('because')
print(last_occur)

new_sen = sen.split( 'because because because' )
print(new_sen)

# 28. Does ''Coding For All' start with a substring Coding?
sen11 = 'Coding For All'
isTrue = sen11.startswith('Coding')
print(isTrue)

# 29. Does 'Coding For All' end with a substring coding?
endWord = sen11.endswith('Coding')
print(endWord)

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sen12 = '   Coding For All      '
remove_whitespace = sen12.strip()
print(remove_whitespace)
# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
str2 = '30DaysOfPython'
str3 = 'thirty_days_of_python'
print(str2.isidentifier()) #False
print(str3.isidentifier()) #True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pylibraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_w = '#'.join(pylibraries)
print(join_w)

# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

new_line1 = 'I am enjoying this challenge.'
newp = new_line1.split()
sep_line1 = '\n'.join(newp)
print(sep_line1)

new_line2 = 'I just wonder what is next.'
newpp = new_line2.split()
sep_line2 = '\n'.join(newpp)
print(sep_line2)


# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

'''
str4 = 'Name      Age     Country   City'
list11 = str4.split()
new_list = '\t'.join(list11)
print(new_list)

str5 = 'Asabeneh  250     Finland   Helsinki'
list12 = str5.split()
new_list1 = '\t'.join(list12)
print(new_list1)
'''

# 35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
r = 10
print(f'radius = {r}')
print(f'area = 3.14 * radius ** 2')
print(f'The area of a circle with radius {r} is {3.14 * r *r} meters square.')


# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
'''

a1 = 8
b1 = 6
print(f'{a1} + {b1} = {a1 + b1}')
print(f'{a1} - {b1} = {a1-b1}')
print(f'{a1} * {b1} = {a1*b1}')
print(f'{a1} / {b1} = {a1/b1}')
print(f'{a1} % {b1} = {a1 % b1}')
print(f'{a1} // {b1} = {a1 // b1}')
print(f'{a1} ** {b1} = {a1 ** b1}')

'''
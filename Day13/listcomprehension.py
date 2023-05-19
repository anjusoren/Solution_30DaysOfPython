# Exercises: Day 13

# 1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negandzero = [i for i in numbers if i<=0]
#print("numbers are : ", negandzero)

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for row in list_of_lists for num in row]
flattened_list = [num for row in flatten_list for num in row]
#print(flattened_list)
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 4. Using list comprehension create the following list of tuples:

list1 = [(0, 1, 0, 0, 0, 0, 0),
 (1, 1, 1, 1, 1, 1, 1),
 (2, 1, 2, 4, 8, 16, 32),
 (3, 1, 3, 9, 27, 81, 243),
 (4, 1, 4, 16, 64, 256, 1024),
 (5, 1, 5, 25, 125, 625, 3125),
 (6, 1, 6, 36, 216, 1296, 7776),
 (7, 1, 7, 49, 343, 2401, 16807),
 (8, 1, 8, 64, 512, 4096, 32768),
 (9, 1, 9, 81, 729, 6561, 59049),
 (10, 1, 10, 100, 1000, 10000, 100000)]


flat_list = [num for row in list1 for num in row]
#print(flat_list)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

flatterned_countries = [[country[0].upper(),country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]
#print(flatterned_countries)

# 5. Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
country_dicts = [{'country': country[0].upper(), 'city': country[1].upper()} for sublist in countries for country in sublist]
print(country_dicts)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
concatenated_list = [[name[0] + ' ' + name[1]] for sublist in names for name in sublist]
print(concatenated_list)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
#lambda function
lamfunc = lambda x1,x2,y1,y2 : (y2 - y1)/ (x2 - x1)
slope = lamfunc(2, 3, 5, 7)
print(slope)

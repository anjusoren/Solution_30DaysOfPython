# Exercises: Day 5

# Exercises: Level 1

# 1. Declare an empty list
new_list = list()
print(type(new_list))

# 2. Declare a list with more than 5 items
n_list = ['Ana',23,'yellow','cola',45.9,'lion']
print(type(n_list))

# 3. Find the length of your list
print(len(n_list))

# 4. Get the first item, the middle item and the last item of the list
print("First item : ",n_list[0])
print("Middle item : ", n_list[2])
print("Last Item : ", n_list[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types  = ["Anju Soren", 26, 150.0, "unmarried","Ranchi"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies =[ "Facebook", "Google", "Microsoft","Apple","IBM","Oracle","Amazon"]

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print("First Company : ", it_companies[0])
print("Middle Company : ",it_companies[3])
print("Last Comany : ",it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies.insert(2,"Blue Mind")
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Spotify")

# 12. Insert an IT company in the middle of the companies list
print(len(it_companies))
it_companies.insert(4, "Flipkart")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
upper_case = it_companies[1].upper()
print(upper_case)

# 14. Join the it_companies with a string '#;  '
join_companies = "#".join(it_companies)
print(join_companies)

# 15. Check if a certain company exists in the it_companies list.
print("IBM" in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_three_companies = it_companies[0:3]
print(first_three_companies)

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-4:-1]
print(last_three_companies)

# 20. Slice out the middle IT company or companies from the list
length_c = len(it_companies)
print(length_c)
print("Middle_element : ",it_companies[5])

# 21. Remove the first IT company from the list
it_companies.pop()
print(it_companies)

# 22. Remove the middle IT company or companies from the list
del it_companies[5]
print(it_companies)

# 23. Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
'''
del it_companies
print(it_companies)
'''

# 26. Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

languages = front_end + back_end
print(languages)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = languages.copy()
print(full_stack)



# Exercises: Level 2
# 1. The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]

# 2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# 3. Find the median age (one middle item or two middle items divided by two)
print("Number of items in the list : ", len(ages))
middle_index = len(ages) / 2
print(middle_index)
m = int(middle_index)
print(ages[m-1])

# 4. Find the average age (sum of all items divided by their number )
sum = 0
for i in ages :
    sum = sum + i
print("sum of all ages : ", sum)

average_ages = sum / len(ages)
print(average_ages)

# 5. Find the range of the ages (max minus min)
ages.sort()
print(ages)
max_ages = ages[0]
min_ages = ages[-1]
print(f'Range of ages : {max_ages} - {min_ages}')

# 6. Compare the value of (min - average) and (max - average), use abs() method
val_min = abs(min_ages - average_ages)
print(val_min)

val_max= abs(max_ages - average_ages)
print(val_max)

# 7. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("Length of the countries list : ", len(countries))
midd = int(len(countries) / 2)
print(countries[midd])

# 8. Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(countries[0:4])
print(countries[4:])

# 9. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
print("First three countries : ",countries[0:3])
print("Scandic countries : ",countries[3:])
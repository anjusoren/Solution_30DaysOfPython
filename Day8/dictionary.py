# Exercises: Day 8

# 1. Create an empty dictionary called dog
dog = {}
print(type(dog))

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Lola'
dog['color'] = 'Brown'
dog['breed'] = 'German'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Anju',
    'last_name': 'Soren',
    'gender' : 'female',
    'age': 26,
    'marital_status': 'unmarried',
    'skills':['coding','reading','reading'],
    'country':'India',
    'city':'Ranchi'
}
print(student)

# 4. Get the length of the student dictionary
print("Length of student dictionary : ",len(student))

# 5. Get the value of skills and check the data type, it should be a list
print("Value of skills : ",student['skills'])
print("Type of skills : ",type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'] = ['drawing','carpentary']
print("Value of skills : ",student['skills'])

# 7. Get the dictionary keys as a list
new_list  = list(student)
print("Get the keys as list : ",new_list)

# 8. Get the dictionary values as a list
new_value_list = list(student.values())
print("Get the dictionary values as list :",new_value_list)

# 9. Change the dictionary to a list of tuples using items() method
new_list_items = student.items()
print("new List : ",new_list_items)

# Delete one of the items in the dictionary
del student['last_name']
print("After deleting an item from student dictionary : ", student)

# Delete one of the dictionaries
del student
print("After deleting student dictionary : ", student)
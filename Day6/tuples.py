# Exercises: Day 6

# Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Lily","Rose","Daisy","Nina")
brothers = ("Will","Smith","Kausik","Leon")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# 4. How many siblings do you have?
numbers_of_siblings = len(siblings)
print(numbers_of_siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents  = ('Will Smith','Lila Smith')
family_members = parents + siblings



# Exercises: Level 2

# 1. Unpack siblings and parents from family_members
print(family_members)
parents_s = family_members[0:2]
print(parents_s)
siblings_s = family_members[3:]
print(siblings_s)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple','Litchi','Orange','Banana','JackFruit')
vegetables = ('Potato','Brinjal','Capsicum','Onion',)
animal_products = ('Egg','Milk','Cheese')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = int(len(food_stuff_tp)/2)
print(mid)
middle_item1 = food_stuff_tp[5]
middle_item2 = food_stuff_tp[6]
print(middle_item1, middle_item2)

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[0:3]
print("First three items : ", first_three_items)
last_three_items = food_stuff_lt[-3 : ]
print(last_three_items)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp)

# 7. Check if an item exists in tuple:
# 8.Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

# 9. Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
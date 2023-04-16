# Exercises: Day 7

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}



# Exercises: Level 1

# 1. Find the length of the set it_companies
length_of_it_companies = len(it_companies)
print("Length of it_companies :",length_of_it_companies)

# 2. Add 'Twitter' to it_companies
'''
it_companies.add("Twitter")
print(it_companies)
'''

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Deep Blue","Spotify","Flipkart"])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove("Spotify")
print(it_companies)

# What is the difference between remove and discard
'''
Both remove and discard is used to remove items from the set.
But if the item is not found, remove() method will raise errors, so it is good to check if the item exist in the given set or not.
However, discard() method does not raise any errors.
'''


# Exercises: Level 2

# 1. Join A and B
C = A.union(B)
print("Joined sets : ",C)

# 2. Find A intersection B
D = A.intersection(B)
print("A intersection B : ",D)

# 3. Is A subset of B
E = A.issubset(B)
print("Is A subset of B : ",E)

# 4. Are A and B disjoint sets
F = A.isdisjoint(B)
print("Is A and B disjoint sets : ",F)

# 5. Join A with B and B with A
A.union(B)
B.union(A)

# 6. What is the symmetric difference between A and B
G = A.symmetric_difference(B)
print("Symmetric Difference between A and B : ",G)

# 7. Delete the sets completely
'''
del A 
del B
print(A)
print(B)

'''


# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print(ages)

# 2. Explain the difference between the following data types: string, list, tuple and set
''' 
String - String is a collection of alphabets, words or other characters.
List - List is a collection which is ordered and changeable(modifiable). It allows duplication.
Tuple - Tuple is a collection which is ordered and unchangeable or unmodifiable.It allows duplicate members.
Set - Set is a collection which is unordered, unindexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
'''


# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sen1 = 'I am a teacher and I love to inspire and teach people'
set1 = sen1.split(" ")
set2 = set(set1)
print("Unique Words : ",set2)
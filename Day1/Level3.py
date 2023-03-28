# Exercise: Level 3
# 1. Write an example for different Python data types such 
# as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
from math import sqrt


print(3) #integer
print(2.5) #float
print(2+ 4j) #complex
print('Air') #string
print(True) #boolean
print(['World','Alien','Space']) #list
print(('roads','pair','monkey','cake')) #tuple
print({'sea','water','deep','whale'}) #set
print({
    'name':'Anju',
    'surname':'Soren',
    'country':'India'
})


# 2. Find an Euclidian distance between (2, 3) and (10, 8)
x1 , y1 = 2 , 3
x2 , y2 = 10, 8

euclidian_distance = sqrt( (x2 - x1)**2 + (y2 - y1)**2)
print(euclidian_distance)


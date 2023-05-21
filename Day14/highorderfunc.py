# Exercises: Day 14

from functools import reduce


#countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# 1. Explain the difference between map, filter, and reduce.
# map() function is a built-in function that takes a function and iterable as parameter
# syntax
# map(function, iterable)

# filter() function calls the specified function which returns boolean for each item of the specified iterable(list). It filters the items that satisfy the filtering criteria.
# syntax
# filter(function, iterable)

# reduce() function takes two parameters, a function and an iterable. However it does not return another iterable, instead it returns a single value.


# 2. Explain the difference between higher order function, closure and decorator

# higher order function are functions that can manipulate and use other functions,
# closures are functions that remember variables from their lexical scope,
# and decorators modify the behavior of functions by wrapping them with other functions.

# 3. Define a call function before map, filter or reduce, see examples.
# 'call' function can be used as a way to invoke higher-order functions with different functions and arguments
def call(func, *args, **kwargs):
    # a helper function to call the given function with the provided arguments
    return func(*args, *kwargs)

#example usage of call function
def square(num):
    return num ** 2

numbers = [1,2,3,4,5]

squared_numbers = call(map, square, numbers)
filtered_numbers = call(filter,lambda x:x%2 == 0, numbers)
sum_of_numbers = call(reduce, lambda x,y : x + y, numbers)

# print(list(squared_numbers))
# print(list(filtered_numbers))
# print(sum_of_numbers)

# 4. Use for loop to print each country in the countries list.
# for country in countries:
#     print(country)

# 5. Use for to print each name in the names list.
# for name in names :
#     print(name)

# 6. Use for to print each number in the numbers list.
# for number in numbers :
#     print(number)


# Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

new_country_list = map(lambda x : x.upper() , countries)
# print(list(new_country_list))

# 2. Use map to create a new list by changing each number to its square in the numbers list
new_squared_list = map(lambda x: x**2 , numbers)
# print(list(new_squared_list))

# 3. Use map to change each name to uppercase in the names list
new_name_list = map(lambda x : x.upper(), names)
# print(list(new_name_list))

# 4. Use filter to filter out countries containing 'land'.
def contain_land(country):
    if 'land' in country.lower():
        return country

land_countries = filter(contain_land , countries)
#print(list(land_countries))

# 5. Use filter to filter out countries having exactly six characters.
def sixcharcountry(country):
    if len(country)==6:
        return country
    
sixchar = filter(sixcharcountry,countries)
#print(list(sixchar))

# 6. Use filter to filter out countries containing six letters and more in the country list.
def sixormore(country):
    if len(country)>=6:
        return country
sixormorel = filter(sixormore, countries)
#print(list(sixormorel))

# 7. Use filter to filter out countries starting with an 'E'
def startswithe(country):
    if country.startswith('E'):
        return country
starte = filter(startswithe, countries)
#print(list(starte))

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
new_num = reduce(lambda acc , x: acc + [x*2], filter(lambda x : x%3==0, map(lambda x: x*2, numbers)),[])
#print(new_num)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_list(new_list):
    return list(filter(lambda x: type(x)==str, new_list))
#print(get_string_list([1,'soup',2,3,'freeze','girl']))

# 10. Use reduce to sum all the numbers in the numbers list.
sum_of_all = reduce(lambda x,y :x+y, numbers)
#print(sum_of_all)

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
result = reduce(lambda acc, country: f"{acc}, {country}", countries)
sentence = f"{result} are north European countries."
#print(sentence)

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
countries1 = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];


# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_by_starting_letter():
    country_counts = {}
    for country in countries1:
        starting_letter = country[0].upper()
        if starting_letter in country_counts :
            country_counts[starting_letter] += 1
        else:
            country_counts[starting_letter] = 1
    return country_counts

#print(count_by_starting_letter())

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten():
    return countries1[:10]

#print(get_first_ten())

# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten():
    return countries1[-10:]

print(get_last_ten())

# Exercises: Level 3

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# a. Sort countries by name, by capital, by population
# b. Sort out the ten most spoken languages by location.
# c. Sort out the ten most populated countries.
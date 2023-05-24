# Exercises: Day 19

# Exercises: Level 1

# 1.Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
from itertools import count
import json

def count_lines_and_words(file_path):
    line_count = 0
    word_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            
    return line_count, word_count

obama_file_path = './Day19/data/obama_speech.txt'
olines,owords = count_lines_and_words(obama_file_path)

# print("Number of lines in Obama speech : ", olines)
# print("Number of words in Obama speech : ", owords)
    
mobama_file_path = './Day19/data/michelle_obama_speech.txt'
molines,mowords = count_lines_and_words(mobama_file_path)

# print("Number of lines in Michelle Obama speech : ", molines)
# print("Number of words in Michelle Obama speech : ", mowords)
    
donald_file_path = './Day19/data/donald_speech.txt'
dlines,dwords = count_lines_and_words(donald_file_path)

# print("Number of lines in Donald speech : ", dlines)
# print("Number of words in Donald speech : ", dwords)
    
dm_file_path = './Day19/data/melina_trump_speech.txt'
dmlines,dmwords = count_lines_and_words(dm_file_path)

# print("Number of lines in Melina speech : ", dmlines)
# print("Number of words in Melina speech : ", dmwords)
    
# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]

def most_spoken_languages(filename, num_languages):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        
    language_count = {}
    
    for country in data :
        languages = country['languages']
        for language in languages:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
                
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    top_languages = sorted_languages[:num_languages]
    
    return top_languages

filename = './Day19/data/countries_data.json'
num_languages = 10
result = most_spoken_languages(filename, num_languages)
#print(result)

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))

# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]

# # Your output should look like this

# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]

def top_densely_populated_countries(filename, num_countries):
    with open(filename,'r', encoding='UTF-8') as file:
        data = json.load(file)
    countries =[]
    
    for country_data in data:
        population = country_data['population']
        
        if population:
            countries.append((population, country_data['name']))
            
    sorted_countries = sorted(countries, key=lambda x: x[0], reverse=True)
    top_countries = sorted_countries[:num_countries]
    
    return top_countries


num_countries = 3
result1 = top_densely_populated_countries(filename, num_countries)
#print(result1)
    
# Exercises: Level 2

# 1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# 2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
# 3. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
# 4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
# 5. Find the 10 most repeated words in the romeo_and_juliet.txt
# 6. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript

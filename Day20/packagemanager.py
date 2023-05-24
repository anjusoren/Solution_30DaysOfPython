# Exercises: Day 20

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests
from collections import Counter
import re

def find_most_frequent_words(url, num_words):
    response = requests.get(url)
    text = response.text
    
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    
    words = text.split()
    word_counts = Counter(words)
    
    most_frequent_words = word_counts.most_common(num_words)
    
    return most_frequent_words

url = "http://www.gutenberg.org/files/1112/1112.txt"
num_words = 10
result = find_most_frequent_words(url, num_words)
#print(result)

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
import statistics

def analyze_cats_data(api_url):
    #fetch the data from api
    response = requests.get(api_url)
    cats_data = response.json()
    
    #extract weights and lifespan data
    weights = []
    lifespans = []
    breed_countries = {}
    
    for cat in cats_data:
        if 'weight' in cat:
            weight = float(cat['weight']['metric'].split()[0])
            weights.append(weight)
            
        if 'life_span' in cat:
            lifespan = int(cat['life_span'].split()[0])
            lifespans.append(lifespan)
            
        if 'origin' in cat and 'name' in cat:
            country = cat['origin']
            breed = cat['name']
            if country in breed_countries:
                breed_countries[country].append(breed)
            else:
                breed_countries[country] = [breed]
                
    #calculate weight statistics
    weight_min = min(weights)
    weight_max = max(weights)
    weight_mean = statistics.mean(weights)
    weight_median = statistics.median(weights)
    weight_stddev = statistics.stdev(weights)
    
    #calculate lifespan statistics
    lifespan_min = min(lifespans)
    lifespan_max = max(lifespans)
    lifespan_mean = statistics.mean(lifespans)
    lifespan_median = statistics.median(lifespans)
    lifespan_stddev = statistics.stdev(lifespans)
    
    #create frequency table of country and breed
    frequency_table = {}
    
    for country, breeds in breed_countries.items():
        breed_count = len(breeds)
        frequency_table[country] = breed_count
        
        return (weight_min, weight_max, weight_median, weight_stddev,
                lifespan_min, lifespan_max, lifespan_mean, lifespan_median, lifespan_stddev, frequency_table)
cats_api = 'https://api.thecatapi.com/v1/breeds'
results = analyze_cats_data(cats_api)
(weight_min, weight_max, weight_median, weight_stddev,lifespan_min, lifespan_max, lifespan_mean, lifespan_median, lifespan_stddev, frequency_table) = results


#   i. the min, max, mean, median, standard deviation of cats' weight in metric units.
print("Weight Statistics:")
print("Minimum weight :", weight_min, "kg")
print("Maximum weight :", weight_max, "kg")
#print("Mean:", weight_mean, "kg")
print("Median:", weight_median, "kg")
print("Standard Deviation:", weight_stddev, "kg")

#   ii. the min, max, mean, median, standard deviation of cats' lifespan in years.
print("Lifespan Statistics:")
print("Minimum lifespan :", lifespan_min, "years")
print("Maximum lifespan :", lifespan_max, "years")
print("Mean:", lifespan_mean, "years")
print("Median:", lifespan_median, "years")
print("Standard Deviation:", lifespan_stddev, "years")

#   iii. Create a frequency table of country and breed of cats
print("frequency table of country and breed : ")
for country,breed_count in frequency_table.items():
    print(country, ':', breed_count)
    
# 3. Read the countries API and find
def analyze_countries_data(api_url):
    #fetch the data from the api
    response = requests.get(api_url)
    countries_data = response.json()
    
    #to find 10 largest countries 
    largest_countries = sorted(countries_data, key=lambda x: x['area'], reverse=True)[:10]
    
    #to find 10 most spoken languages
    spoken_languages = {}
    
    for country in countries_data:
        for language in country['languages']:
            if language['name'] in spoken_languages:
                spoken_languages[language['name']] +=1
            else:
                spoken_languages[language['name']] = 1
    
    most_spoken_languages = sorted(spoken_languages.items(), key=lambda item: item[1], reverse=True)[:10]
    
    #calculate the total number of languages in the countries API
    total_languages = len(spoken_languages)
    
    return largest_countries, most_spoken_languages, total_languages

countries_api = 'https://restcountries.eu/rest/v2/all'
results2 = analyze_countries_data(countries_api)

largest_countries, most_spoken_languages, total_languages = results2


                
    
#   i. the 10 largest countries
print("10 largest countries : ")
for country in largest_countries:
    print(country['name'])

#   ii. the 10 most spoken languages
print("10 most spoken languages: ")
for language, count in most_spoken_languages:
    print(language, ':', count)
    
#   iii. the total number of languages in the countries API
print("Total number of languages : ", total_languages)
# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

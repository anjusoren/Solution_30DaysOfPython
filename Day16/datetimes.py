# Exercises: Day 16

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
#print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f'day : {day} , month : {month} , year : {year} , hour : {hour} , minute : {minute} , timestamp : {timestamp}')

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
currentdate = now.strftime("%m/%d/%Y, %H:%M:%S")
print(currentdate)

# 3. Today is 5 December, 2019. Change this time string to time.
time_string = '5 December, 2019'
datetime_object = datetime.strptime(time_string, "%d %B, %Y")
print(datetime_object)

# 4. Calculate the time difference between now and new year.
from datetime import date
today = date(year=2023, month=5, day=21)
new_year = date(year=2024, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time difference between now and new year : ', time_left_for_newyear)

# 5. Calculate the time difference between 1 January 1970 and now.
new_time = date(year=1970, month=1, day=1)
time_difference = today - new_time
print("Time Difference : ", time_difference)
# 6. Think, what can you use the datetime module for? Examples:
    # Time series analysis
    # To get a timestamp of any activities in an application
    # Adding posts on a blog
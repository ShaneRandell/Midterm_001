## Part 2 ##

# Calculate how much time on the planet you have lived in seconds

import time

sec = str() # setting sec = to a string
print("Calculate how old you are in seconds\n")     # printing to the screen to explain the program
print("Enter your age")     # asking for a user input
year = float(input())   # converting the input to a float
print("Enter how many months since your birthday") # asking for a user input
month = float(input())  # converting the input to a float

Days = ((year*12)*30)     # determing
# the number of days the user has been alive
Day2 = Days + (month *30)   # add the days of months to the total days
sec = (Day2*86400)          # multiply the days alive by seconds in a day to get the number of seconds alive

print("you have been alive for")   # printing the final answer
print(sec,"seconds")







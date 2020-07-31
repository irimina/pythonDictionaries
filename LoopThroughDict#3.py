# Checking if a value exists using .values()

# Create a dictionary of some of the Code Avengers level 1 Python lessons
ca_lessons = {1.2: 'Strings 1', 1.6: 'Turtle Graphics', 1.13: 'Boolean'}

# Ask the user to look up an item
title = input("Enter the title of the lesson you would like to look up: ").strip().title()

# Check if an item is in the dictionary
if title in ca_lessons.values():
  print("Yes,",title," is in the Level 1 Python Course")
else:
  print("Sorry, that lesson does not appear to be in the course.")
  
######################################################################

'''
Using .get() to check if an item exists safely
If we try to access an item in a list using a key that doesn't exist, we will get a KeyError. We could wrap our code in try/except to handle the KeyError, but with a dictionary we can also use a function called .get().

This .get() will return the value for the given key if it exists, or False if it doesn't exist. We can also set a specific value to return instead of false if it doesn't exist:

us_states = {'alaska':'AK', 'alabama': 'AL', 'arizona': 'AZ'}
state = us_states.get("colorado") # state = False
state = us_states.get("alaska")   # state = "AK"
state = us_states.get("colorado", "No value") 
# state = "No value"

'''

# Create a dictionary of player usernames and scores
player_scores = {'CoolKiwi': 1125, 'Avenger909': 1275, 'InfamousCandyKid': 1050}

# Safely check if a player is on the leaderboard
player = input("Which username would you like to look up? ").strip()

#Find a user's score
score = player_scores.get(player)

if not score: #Checks if score is False
  print("Sorry, {} is not on the leaderboard".format(player))
else:
  print("{}'s score is {}".format(player, score))

######################################################################

'''
Looping through a dictionary to access or print out keys
In this lesson you will learn a range of ways to access the data in a dictionary using loops and other Python features.

Let's look first at the equivalent of printing a list using:

for item in my_list:
  print(item)
We can do exactly this if we just want to access the keys in the dictionary:

for item in my_dict:
  print(item)
Remember that the item variable (or whatever name you use) is just like any other variable. We can do anything with it, although we are just printing it in these examples.


'''







######################################################################








######################################################################

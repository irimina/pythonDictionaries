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
# Create a dictionary of calorie values per 100g of common foods.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}

# Print out each key from the dictionary
for food in calorie_values:
  print(food)

######################################################################
# Using loops to print both keys AND values

'''
If we want to print out (or use) both the keys and the values from the dictionary, we just need to give each of them a name and use the format:
for k, v in my_dict.items():
  print(k, v)
Where k is the name you choose for the keys, and v is the name you choose for the values. Note that k and v will actually work, 
they are just not very well-named variables.
'''

# START
# Create a dictionary of calorie values per 100g of common foods.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}

# Print out each key from the dictionary
for food in calorie_values:
  print(food)

# Print out each key AND value from the dictionary



# Print out each key and value in a string 



# END

# Create a dictionary of calorie values per 100g of common foods.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}

# Print out each key from the dictionary
for food in calorie_values:
  print(food)

# Print out each key AND value from the dictionary
for food, calories in calorie_values.items():
  print(food, calories)

######################################################################
# Adding values to a dictionary

# Create a dictionary of student details
student1 =  {"name": "Sally", "age": "19", "occupation": "student", "hometown": "Auckland", "mobile":"012 345 6789"}

# Add new details
print(student1)

######################################################################
'''
Modifying existing values
To change existing values, we can use both methods we already learned for adding values.

knight = {'name': 'Magdalin the Conquerer', 'weapon': 'Warhammer', 'warcry': 'Ni!', 'speed': 6, 'strength': 8}
To change Magdalin's warcry we just set it equal to something new:

knight['warcry'] = "Ekki-ekki-ekki-ptang-zoom-boing!"
To change more than one value (and you can add new ones at the same time):

knight.update({'speed': 7, 'strength': 9})

'''

'''
Removing values with del and .pop()
To remove values from a dictionary, we can use .pop() like we did for lists. Instead of passing in the index or number of the value though, we pass in the key:

knight.pop('age')
This will return the value that you have removed so you can store it in a variable, or add it to a different dictionary or the like.

If we just want to delete something altogether, however, we use del. This has no brackets, it is just used like this:

#Delete age
del knights['age']
'''

# Student details
student1 = {'name':'Sally','age':20,'occupation':'developer','hometown':'Auckland','mobile':'012 345 6789','height':'1.56','fav_food':'pizza','fav_color':'lime green'}

# Remove mobile using .pop() and store as mobile
mobile = student1.pop('mobile')
print(mobile)
 
# Remove fav_food and hometown using del
del student1['fav_food']
del student1['hometown']
 
# Print dictionary
print(student1)


######################################################################




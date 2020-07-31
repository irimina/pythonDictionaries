

'''
Creating dictionaries with strings.
Let's take a closer look at creating dictionaries with strings.

We always need to give our dictionary a logical, Pythonic name using the same rules as variables.

Our key/value pairs go inside curly brackets {} comma , separated.

We can use strings for both the key and the values in a dictionary:

my_dict = {'key': 'value', 'another key': 'another value'}
'''


'''
Create a dictionary called us_states that stores the first 3 (alphabetical) states in the USA and their abbreviations as listed below.
Create a dictionary called websites on line 5 that stores the names and URLs of 3 websites as listed below.

'''

#START

# Create a dictionary of the first 3 States in the USA and their abbreviations.


# Create a dictionary of website names and addresses



#END
# Create a dictionary of the first 3 States in the USA and their abbreviations.
us_states= {"alabama":"AL", "alaska":"AK", "arizona":"AZ" }

# Create a dictionary of website names and addresses
websites={"google":"http://google.com", "facebook": "http://facebook.com", "twitter": "http://twitter.com"}

################################################################################
'''
Creating dictionaries with integers
So, as you have seen we can use strings as both keys and values in a dictionary.
We can also use integers as either keys or values as we'll see later in this lesson.

Calorie Values:

butter - 770
cornflakes - 364
celery - 6
strawberries - 26
Scores:

CoolKiwi - 1125
Avenger909 - 1275
InfamousCandyKid - 1050
'''

# Create a dictionary of calorie values per 100g of common foods.

  
# Create a dictionary of player usernames and scores

#END
# Create a dictionary of calorie values per 100g of common foods.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}
  
# Create a dictionary of player usernames and scores
player_scores = {'CoolKiwi': 1125, 'Avenger909': 1275, 'InfamousCandyKid': 1050}
################################################################################
# Creating dictionaries with floats
# We can also use floats as both keys and values.

# START
# Create a dictionary of some of the Code Avengers level 1 Python lessons


# Create a dictionary of heights of knights

#END

# Create a dictionary of some of the Code Avengers level 1 Python lessons
ca_lessons = {1.2: 'Strings 1', 1.6: 'Turtle Graphics', 1.13: 'Boolean'}
 
# Create a dictionary of heights of knights
heights_of_knights = {'Godfree the Eager': 1.76, 'Otto the Heroic': 1.8, 'Magdalin the Conquerer': 1.75, 'Isabel the Invincible': 1.7}


################################################################################
'''
Using other types of data in a dictionary
We can also use other types of data in a dictionary, including Boolean values, lists and calculations, although not all will work as both keys and values.

Boolean values and lists can be used as values.

Calculations can be used as either keys or values, 
but when you try to print out a value that is a calculation it is the result of the calculation that is shown.

Take a look at the random collection of data in the dictionary in the editor!
'''

#START
# A random dictionary! It is common to write more complex dictionaries on new lines like this to make them easier to read.
# They won't normally be this confusing!
random_dict = {1: 'apple', 
        2.7: 'banana', 
        'three': True, 
        'four': [1, 2, 3], 
        5: 6 * 5, 
        3 * 6: 'date'}

#Print statements

#END
# A random dictionary! It is common to write more complex dictionaries on new lines like this to make them easier to read.
# They won't normally be this confusing!
random_dict = {1: 'apple', 
        2.7: 'banana', 
        'three': True, 
        'four': [1, 2, 3], 
        5: 6 * 5, 
        3 * 6: 'date'}

#Print statements
print(random_dict[2.7])
print(random_dict["four"])

print(random_dict[5])
print(random_dict[3*6])



################################################################################

'''
Accessing values in a dictionary using the key
In the last lesson we printed some values from the dictionary using the item's key, or the first part of the pair that makes up the item e.g.:

print(websites['facebook'])
We can use websites['facebook'] like any other variable.

If the key is a string we write it inside quotes. If it's an integer, float or Boolean then there's no need to wrap it in quotes.

'''
# Create a dictionary of website names and addresses
websites = {'google': 'http://google.com', 'facebook': 'http://facebook.com', 'twitter': 'http://twitter.com'}

# Print statements:
# Print statements:
print(websites['google'])
print("The URL for Twitter is:", websites['twitter'])

################################################################################

'''
Checking if a key (item) exists using .items()
With lists, we could use an if statement to check if an item was in the list:

if "apple" in fruit_list:
  #Do something
We can do a similar thing with dictionaries, and this will check if a certain KEY exists:

if "apple" in fruit_dict:
  print(fruit_dict['apple'])
In the places where we are using the string apple we could also use a variable that contains the string apple:

item = "apple"
if item in fruit_dict:
  print(fruit_dict[item])
In the editor is some code that does this, but it will ask the user for an item and then look up the calorie value in the dictionary.
'''

# using input
# Create a dictionary of calorie values per 100g of common foods.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}

# Ask the user to look up an item
item = input("Enter the name of the food item you would like to look up: ").strip().lower()

# Check if an item is in the dictionary
if item in calorie_values:
  print("Yes the calorie value is",item, calorie_values[item])
  
else:
  print("Sorry, that item is not in the dictionary")
################################################################################


################################################################################

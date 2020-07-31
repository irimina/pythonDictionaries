

'''
Introduction to dictionaries
Dictionaries are another type of collection or indexed data structure similar to lists. You can look up values in a collection to use them in your code.

In the code editor are three example dictionaries showing you how to create them. Here are some important things about dictionaries:

Dictionaries are wrapped in curly brackets {}
Items in a dictionary are separated by commas ,
Dictionaries can contain strings, integers, floats, Booleans, lists or other dictionaries
Strings get wrapped in quotes like always
Each item in a dictionary has a key and a value written in the format 'key': value

'''


#START

# Dictionary storing English and Spanish words (strings)
english_to_spanish = {'table': 'mesa', 'apple': 'manzana', 'dog': 'perro'}

# Dictionary storing people's ages (integers)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4}

#A dictionary of favotires (mixed values)
my_favorites = {'color':'blue', 'food': 'butter paneer', 'decimal': 3.14159}


#END
# Dictionary storing English and Spanish words (strings), add clock with the translation reloj
english_to_spanish = {'table': 'mesa', 'apple': 'manzana', 'dog': 'perro', 'clock':'reloj'}

# Dictionary storing people's ages (integers), add your name with your age
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, "Iulian":40}

#A dictionary of favotires (mixed values) - add number 9
my_favorites = {'color':'blue', 'food': 'butter paneer', 'decimal': 3.14159, "number":9}



################################################################################
'''
Printing values from a dictionary
Just like a list, we can print a whole dictionary by using the name e.g.:

print(ages)
In a list each item has a numerical index, which is a unique value that is assigned to it. 
In a dictionary, however, the index doesn't have to be a number and is also called a key.

This key is used to find the value when you need it.

For example Claire's age is ages['Claire'].

To print a value from a dictionary, we plug the whole lot including the key into our print statement:

print(ages['Claire']) #Prints 24

'''

# START

# Dictionary storing English and Spanish words (strings)
english_to_spanish = {'table': 'mesa', 'apple': 'manzana', 'dog': 'perro', 'clock': 'reloj'}

# Dictionary storing people's ages (integers)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Monty': 68}

#A dictionary of favotires (mixed values)
my_favorites = {'color':'blue', 'food': 'butter paneer', 'decimal': 3.14159, 'number': 9}


#END

# Dictionary storing English and Spanish words (strings)
english_to_spanish = {'table': 'mesa', 'apple': 'manzana', 'dog': 'perro', 'clock': 'reloj'}

# Dictionary storing people's ages (integers)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Monty': 68}

#A dictionary of favotires (mixed values)
my_favorites = {'color':'blue', 'food': 'butter paneer', 'decimal': 3.14159, 'number': 9}

#Printing out values
print(english_to_spanish)

print(ages['Rafael'])

print(my_favorites['food'])

################################################################################
'''
Creating a dictionary with the dict() function
Python has a built-in function that lets us create dictionaries. We just choose a name, and then pass in pairs of keys and values to the function:

my_dict = dict(name = 'Bob', age = 32, hometown = 'Auckland')
This will create the equivalent of this:

my_dict = {'name': 'Bob', 'age': 32, 'hometown': 'Auckland'}
It's not that much faster with a small dictionary, but this can be really handy if you already have 2 lists that correspond to each other, 
and if you remember the zip() function from earlier.
'''

# END
names = ["Sarah", "Jose", "Tane", "Monty"]
fav_foods = ["Apples", "Salad", "Pizza", "Nachos"]

foods_dict = dict(zip(names, fav_foods))

#Print the whole dictionary to see the result
print(foods_dict)

#Print out Jose's favorite food.
print(foods_dict['Jose'])
################################################################################
'''
Modifying values in a dictionary
We can add, modify and delete values from a dictionary using the item's key.

It's important to note here that dictionaries are unordered, so that means there are not 2 options for deleting an item - using its value or its position in the dictionary - like there were with lists.

favorites = {'food': 'apples', 'color': blue}
favorites['number'] = 9 #Adds 'number': 9
favorites['color'] = 'green' #Changes 'color' value
del favorites['food'] #Deletes favorite food.
'''

#START
# Dictionary storing people's ages (integers)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Monty': 68}

# Print a value


# Modify Claire's age


# Add Lisa who is 42


# Delete Monty from the dictionary


#Print the whole dictionary 

# END
# Dictionary storing people's ages (integers)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Monty': 68}

# Print a value
print(ages['Claire'])

# Modify Claire's age
ages['Claire']=25

# Add Lisa who is 42
ages["Lisa"]=42

# Delete Monty from the dictionary
del ages["Monty"]

#Print the whole dictionary 
print(ages)

################################################################################


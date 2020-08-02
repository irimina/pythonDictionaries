
'''
In this lesson we are going to work through an example program that will translate words from English to Maori. 
In this code we will use both a dictionary and functions.

The next lesson will step through some testing and some advice for commenting your code.

Let's get started by building the dictionary and writing the first function.


Word List:

apple: aporo
chair: turu
pen: pene
hello: kia ora
goodbye: ka kite
Menu Text:

Type: 
 '1' to view menu
 '2' to see word list
 '3' to translate a word
 '4' to end program

'''

#START
# English to Maori dictionary


# Menu function


#END

# English to Maori dictionary
WORD_LIST= {"apple": "aporo",
"chair": "turu",
"pen": "pene",
"hello": "kia ora",
"goodbye": "ka kite"}

# Menu function
def menu():
  print("""
  Type: 
 '1' to view menu
 '2' to see word list
 '3' to translate a word
 '4' to end program
  
  """)
  
menu()
##############################################################################
'''
Creating the function to print out the word list
If we look at the menu text, we can see the user has 4 options. We have created the function for option 1 - view menu.

Now let's create the function for option 2 - see word list. 
This function will loop through the dictionary and print out each word and its translation.
'''

#START
# English to Maori dictionary
WORD_LIST = {'apple':'aporo','chair':'turu','pen':'pene','hello':'kia ora','goodbye':'ka kite'}

# Menu function
def menu():
  print("Type: \n",
        "'1' to view menu\n",
        "'2' to see word list\n",
        "'3' to translate a word\n",
        "'4' to end program")

# Show word list function


# END
# English to Maori dictionary
WORD_LIST = {'apple':'aporo','chair':'turu','pen':'pene','hello':'kia ora','goodbye':'ka kite'}
 
# Menu function
def menu():
    print("Type: \n",
          "'1' to view menu\n",
          "'2' to see word list\n",
          "'3' to translate a word\n",
          "'4' to end program")
 
# Show word list function
def show_list():
    for word, translation in WORD_LIST.items():
        print(word.title(), translation))
 
show_list()


##############################################################################






##############################################################################




##############################################################################










'''
Testing the functions
Now that we've tested our menu options, we need to test any other functionality
inside our functions.

Our menu() and show_list() functions only output information and so if they ran
correctly when we tested the menu, they should be fine.
You may want to check that again if you didn't look closely at the output in the
last task!

Our translate mode takes in user input, however, so we'll need to do a bit
more testing on that.

CREATE
Test the menu() and show_list() functions again just to make sure we're getting
the output we expect.
This time choose mode 3 and test the translate() function with an expected value.
Although not an official "boundaries", our borderline cases here are probably
words typed with capital letters. Test a few of these. Fix the bug so it is case
insensitive.
Test the menu(), show_list() and translate() functions again to check the
everything is working well. Then we need to test a couple of words that aren't
in the dictionary.

TIPS
Note: Words that are not in the dictionary are not invalid values as such,
because we would probably expect the user to type those words in at times,
and we allow them to do it, we just give them an error message.
It is still important to make sure your code handles them fine, and that's why
we use the if statement to check the word exists before getting a translation.
'''


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
    print(word.title()," is ",translation, "in Maori")
 
# Translation function
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print(translation,"in Maori is",word.title())
  else:
    print("Sorry that word is not in the dictionary")
        
# Main program
print("Welcome to the English to Maori dictionary")
name = input("What is your name? ").title()
print("Hello", name)
 
# Print menu
menu()
 
# Run program loop
repeat = True
while repeat == True:
 
  # Ask user for input and 
  option = input("What would you like to do? ")
 
  # Check input and run the chosen function
  if option == "1":
    menu()
  elif option == "2":
    show_list()
  elif option == "3":
    word = input("What word would you like to translate? ")
    translate(word.lower())
  elif option == "4":
    print("Goodbye", name,"thanks for using the dictionary!")
    repeat = False
  else:
    print("That wasn't an option")


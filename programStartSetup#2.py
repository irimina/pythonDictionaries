'''
Set up the start of the main program
Ok, so our dictionary and our functions are ready to go.
Now we need to write the main part of our code.

This part will welcome the user and print the menu,
and then we'll need to ask the user what they want to do and do it.
We'll put the last part in a loop so the user can use the different modes
without having to re-run the program.

CREATE
There are a few new comments in the editor. Under the welcoming print statement,
ask the user What is your name? and store it as name.
You can add .title() here if you want a well-formatted name.
Below this print a welcome in the format Hello, Bob with the user's name.
Under the next comment, call the menu() function.
To run the program loop, under the relevant comment, create a variable
called repeat and set it to True.
Write a while loop statement that will run our loop as long as repeat stays True.
Inside the loop, ask the user What would you like to do? and store as option.
Make sure you use strip().
Click RUN and check this welcome segment works (you will get stuck in the loop
but that's OK for now).

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
    print("{} = {}".format(word, translation))

        
# Translation function
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} in Maori is {}".format(word, translation))
  else:
    print("Sorry that word is not in the dictionary")

# Main program
print("Welcome to the English to Maori dictionary")
name= input("What is your name? ").title()

# Print menu
print("Hello", name)

# Run program loop
menu()

# you will get stuck in the loop for now but that's OK
repeat=True
while repeat is True:
  # Ask user for input 
  option=input("What would you like to do? ").strip()
  


'''
Create the translation function
Alright, our translator wouldn't be a translator without a translation function,
so let's build that now.

We will need to pass in a word as a parameter,
then use that word as the key to find the translation,
and print out the translation.

Create a function called translate that takes one parameter word.
Write an if statement that will check if word is in WORD_LIST.
If it is (in the if branch), set a new variable translation equal to the value in WORD_LIST using the key.
Still inside the if branch, print out word and its translation in the format Apple in Maori is aporo.
Create an else branch and print Sorry that word is not in the dictionary as the error message.
Test the function by calling it at the end of the program and passing in apple as a string.

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
        print(word,"in Maoro is", translation)

# Translation function
def translate(word):
  if word in WORD_LIST:
    translation=WORD_LIST[word]
    print(word,"in Maori is.", translation)
  else:
    print("Sorry that word is not in the dictionary")
translate("chair")

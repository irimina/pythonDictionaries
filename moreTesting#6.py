'''
Commenting code for understanding
Our program has some comments in it, and our variables and functions are
pretty well-named so our code is quite easy to understand. However,
there are a few other places we could add some short comments to explain the
code further.

Choose the comment from the list below that best fits each line of code:

Documenting functions with docstrings
When writing code with functions, it's a good idea to make sure there are comments that explain the purpose of the function. This can be done above the function like so:

# Show List function loops through each item in the list so that keys and values can be printed in a user-friendly format
def show_list():
  for word, translation in WORD_LIST.items():
    print("{} = {}".format(word, translation))
We can also put a docstring inside the function, which will
return an explanation of the function when you call help() on the
function name e.g. print(help(show_list)).
These are written as the first line in the function, get wrapped in
triple double quotes: """,
and you can see an example in the menu() function.


QUIZ QUESTIONS - FOR STUDENTS

Who should you think like when testing your program?
typical user,
advanced user
very young child
adult

True or False: You don't need to test functions that only OUTPUT information.
True
False

Which of the following reduces the need to use lots of comments in your code?

well-named variables
well-chosen functions
well-chosen coding structures
all of these


What symbol is used to create a docstring?
""""
#
-






'''


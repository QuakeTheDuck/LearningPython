## M/D/Y 04/25/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1

# The idea of a function is to assign a set of code and variables known as parameters,
# to a single bit of text
# Instead of writing out the code each time you want to exucute it
# You create a function and then call on the function to preform that code

# To begin the function you first need to define it by using 'def' short for define
# Be careful when defining and function, make something unique and memorable
# If called 'time' or certain other things it can interfere with other built-in or imported functions
# the below function is called 'example()'

'''
def example():
    brtrtr        # this is all one block
    trthrhtrhtrd  # within the same function
    hdrthrtdhtr   # this is all one block
    hrdthrdtdthr  # within the same function

newthing # code written down here is not in the function since it is not on the same indent after the colon
'''

# the code will not output anything because it isn't called upon
# when the 'example()' function is called it will run the block it contains
def example():
    print('basic function')
    z = 3+9
    print(z)

example() #! remove the note and rerun code

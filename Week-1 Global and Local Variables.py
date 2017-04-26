## M/D/Y 04/25/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1
#! https://pythonprogramming.net/global-local-variables/

# Written like this 'x' is not global
# It needs to be defined as global
'''
WTF
If 'global x' is written before, or after 'x = 6' it won't work
only inside of the function does global x work
'''
# Some places won't let you use global variables
'''
x = 6

def example():
    global x
    print(x)
    x+=5
    print(x)

example()
'''

# This gets around using global variables BUT it redefines 'x' as 'globx'
x = 6 # define variable

def example(): # define function
#! variables created inside of the function are local and won't work outside of it
    globx = x # redefine variable within the function
    print(globx) # print the variable
    globx+=5 # add 5 to our function and store that sum as the new variable
    print(globx) # print the variable

    return globx # This returns 'globx' to the 'x' it was previously
                 # Allowing everything else to still use x as normal instead of our new globx

x = example()

print(x)

## M/D/Y 04/23/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1
#! Errors are included, ignore them until you reach that part in the lesson
'''
Variables are used to store information to be referenced and manipulated in a computer program
They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves
It is helpful to think of variables as containers that hold information
Their sole purpose is to label and store data in memory
This data can then be used throughout your program
'''

# You define a variable in python by typing it out
# Below 'exampleVar' is the variable it can be written like 'EXAMPLE_VAR', 'Example_Var', 'exampleVar' nearly any way you like
# Remember be consistent
# The exampleVar is camelCasing, because new words or abbreviations are capitalized, or bigger, like a camels hump
# You cannot start a variable with a number
exampleVar = 58

print(exampleVar)
# Above we have the integer '55' which has been put into the variable 'exampleVar'
print(exampleVar + 55)
# Since it is an integer stored inside a variable it can be added as if it were an integer

#

# Variables are very powerful and are used !a lot! there are many thing you can do with them
newVar = 9+33

print(newVar)

print(newVar + exampleVar)

# 'print()' is a function, variables can contain functions

crazyVar = print('whoa')
anotherVar = print(5+9)

print('CLEAR')
print('CLEAR')
'''
Unpacking varibles
'''
# Both 'x' and 'y' are variables
# The '5' and '3' and a list
# The program will read this as 'x = 5' and 'y = 3'
x,y = (5,3)

print(x)
print(y)
print(x+y)
print(x-y)

# ERROR
# Below shows two variables with a list containing three different digits
# This will cause 'ValueError: too many values to unpack'
# For now debug the code, more debugging will be covered further in the future
# Just remember the amount of variables and the amount of items in a list must be equal
x,y = (5,3,8)

print(x)
print(y)
print(x+y)
print(x-y)

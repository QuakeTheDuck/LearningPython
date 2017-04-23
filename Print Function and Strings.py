## M/D/Y 04/23/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## The use of the pound or hashtag is to make a note - alt+3 on the keyboard will add two '##' to the current line or all lines that you have selected
## Notes are used to help organize, understand and debug code
## Debug/Debugging is the term given to the act of finding, removing, and fixing errors and mistakes within code

## CRTL+SHIFT+S is used to save-as with 
## F5 is used to 'Run Module' within Python IDLE(Python 3.6)

######################################################################################################
# !!! There are errors included this is to be corrected by practice !!!
######################################################################################################
# Lets learn about the some functions & strings
# The 'print' you see that is not noted out is a function
# All the text below that is incased in quotes is a string
# str = string

print('This is a string within the print function') # single quote
print("This is a string within the print function") # double quote
print('''This is a string within the print function''') # triple quote


# Below is showing one difference between single and double quotes
# We need to tell the code to ignore the apostrophe in 'They're' by adding an 'escape character' called backslash \
# The 'escape character' because it escapes the functionality of the following character(!!!I THINK!!!)
# Try to RUN the code without the backlash and see the error, this can help for future debugging practice, don't forget to save
print("They're going to the ball game")
print('They\'re going to the ball game')


# Below you see the use of single through triple quotes
# Chances are you won't want to use backslashs like this much, it doesn't look nice
# In the example above you see that it looks better with double quotes
# This example it looks better with single quotes
print("She said \"Hello.\"")
print('She said "Hello."')
print('''She said "Hello."''')

# Triple QUOTES
print('''Here's another example. She said "Hello."''')
# Moving on...


# Concatenation is the operation of joining character strings end-to-end
# Generally concatenation is used to join strings together

# In the first example will notice there is no space
# That is because we didn't tell include a space.
print('Hi'+'there')
print('Hi '+'there')
print('Hi    '+'there')

# You can also concatenate with a comma, this will include a space
print('Hi','there')

# You can replace a string with an integer also known as an 'int'
# An integer is any whole number with no decimal following, 5, 6, -7, 25, 7, 34 are all integers. 3.7, 1.9, and 6.0 are not integers.
print('Hi',5)

# Below is an error, you cannot add an integer to a string
# This can be corrected by turning the integer into a string, try adding quotes around the 5 and RUN
print('Hi'+'5')

print('CLEAR')
print('CLEAR')
print('CLEAR')
# If you REALLY want to add the integer 5 to the string you need to use another 'built in function'
# So far we have used the 'print' function and now we are also going to use the 'str' function
# This is known as a 'string conversion' this converts the integer into a string and adds it to the string
print('Hi '+str(5))
print('Hi '+str(5))

print('CLEAR')
# Below may seem fine but you will encounter an error
# Since the '8' is within a string it cannot be added to the integer '5'
# The new function is 'int'
print(int('8')+5)
print(int('8')+5)

print('CLEAR')
# Remember programmming can be fussy! Below shows '8.5' in the string but it's trying to define it as an integer(int)
# The new function is 'float'
# A 'float' is defined as a number that has digits on both sides of a decimal point like 3.0, 5.9, 7.2
print(float('8.5')+5)
print(float('8')+5)

print('FINished')
#FIN
#FIN
#FIN
#FIN
#FIN


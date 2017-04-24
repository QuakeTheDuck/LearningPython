## M/D/Y 04/24/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1
# More content is being turned into notes
# This is to allow me to retain more of the covered content
#! This means anyone including me looking at this in the future MUST fix the noting to use this properly(terrible idea)

# the 'if' statement is used do whatever code is held within the statement
# the code will be done if the statement is met, if not it will be skipped

#! The 'if' statement is a basic form of logic
'''
x = 5
y = 8

# since x is NOT greater than y the 'if' statement is skips the block under it
# the block being the indented code after the colon
if x > y:
    print('x is greater than y')

# remove the below note and see what happens
'''

'''
if y > x:
    print('y is greater than x')
'''

'''
x = 5
y = 8
z = 5
a = 3

if z < y > x > a:
    print('y is greater than z and greater than x')
'''

x = 5
y = 8
z = 5
a = 3

# You cannot have the below statement read "if z = x:"
# That would be directly asking about varibles are not the content of the variables, integers in this case
# What you do is 'if z == x:
if z == x:
    print('z is less than or equal to x')
#! Have not covered else statements yet but I remembered it

else:
    print('z is greater than x')
# 'if z != x:' Would mean: if z is NOT equal to x do the following block of code

#QUESTION
# Since the error is in the block and the block is not ran
# Will this cause syntax error or not?
'''
x = 55

if x > 100:
    print('syntaxerror!
else:
    print('hi')
'''

# the program will error immediately
# and none of the code will run
# regardless of where the syntax error occurs


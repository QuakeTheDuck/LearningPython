## M/D/Y 04/24/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1


# The idea of the paring is to add another piece of logic to the 'if' statement

# If something is true do this if NOT do this other thing, think about the else statement like NOT
# Straight forward, we define the variables 'x' and 'y'
# Ask if 'x is greater than y' if print that it is greater
# ELSE print that it is not greater

x = 5
y = 8
#! flip the greater than signs and play around
# huh, the first 'if' statement has no impact on the other 'if' or 'else' statement
# this spits out the 'else' statement since the second 'if' statement is not TRUE
if x < y:
    print('x is greater than y')
if x > 55:
    print('55 is greater than x')
else:
    print('x is not greater than y')

# remembered the 'elif' statement

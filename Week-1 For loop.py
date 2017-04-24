## M/D/Y 04/23/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1
##! Learning program is hard and problems often need to be solved, if unsure about anything look for an answer
##! Troubleshooting to find a solution is an extremely important skill

# While and for loops are interchangeable. Preference and consistency matter
# Proper etiquette is enforce by a company if a job is landed
# Tabbing over(right) code: Highlight a section of code or block of code and hit 'TAB' it will tab over the entire highlighted section
# Tabbing over(left) code: Highlight code and use CTRL+[

# The 'While loop' is generally used for finite or infinite tasks
# The 'For loop' is used to generally to be more variable, uncertain time frames

# For loops are often used to iterate(perform/utter repeatedly) through a list
'''
() - Round brackets or parentheses
[] - Square brackets
{} - Curly brackets or braces
<> - Angle brackets or chevrons
'''

# Below shows a variable and a list, previously I wrote that total number of variables must match number of items in a list
# This is true if there are multiple varibles but untrue if there is only one varriable assigned to a list
#? Purpose of square brackets and not round brackets is currently unknown, they both functioned the same in the below example
exampleList = [1,5,6,1,6,7,8,9,345,53,5]
print(exampleList) # This outputs the contents of the list in one line since that is how it is stored inside the variable
# Created a variable call 'eachNumber' below
for eachNumber in exampleList:
    print(eachNumber)


# Notice the lack of indent here, this causes the program to run all of the above code BEFORE it reaches this point
# Indent the below print function to align with the print function above it
print('continue program')

#! New built-in function 'range'
# This function starts are the first number '1' and goes all the way up until, but not including, the last number
for x in range(1,11):
    print(x)
'''
Challenge
Using the following: l = [5,6,2,1,4], create a for loop that cycles through each element of the l variable list,
adding 5 and printing out the result to console.
'''
#My answer
one = [5,6,2,4]
for eachNumber in one:
    print(eachNumber+5)
    
print('CLEAR')

'''
I'll call this one a "bonus" challenge for anyone first starting out with the basics of Python.
There is a way to do for loops in one line.
Don't feel bad if you skip this one while you are just trying to learn the basics, but, for you brave folks: 
Convert the following multi-line for loop into a single line:
for x in range(10):
    print(x)

'''
#My answer
for hi in range(10): print(hi)

print('CLEAR')
#His answer
[print(x) for x in range(10)]




print('FINished')


#Question sent
'''
Thank you.
Running Python 3.6.1
From "For Loop Python Tutorial"
Challenge: Convert the following multi-line for loop into a single line:
for x in range(10):
    print(x)

I wrote:
for x in range(10): print(x)

You wrote:
[print(x) for x in range(10)]

Output was the same for both of these in the shell. 3.6.1
In there any adverse effects that could come from my way since the output was the same? If so could you give me an example.
'''

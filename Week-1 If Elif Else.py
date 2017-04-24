## M/D/Y 04/24/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1

# Adding more logic!

x = 5
y = 10
z = 22

if x > y: # IT IS NOT
    print('x is greater than y') 
elif x < z: # IT IS
    print('x is less than z') # SO THIS IS RAN
# Since the above 'elif' statement is ran it breaks/stops the rest of the code from being ran
# Once an 'elif' finds something thats true it wont keep searching
elif 5 > 2:
    print('5 is greater than 2')
else:
    print('if an elif(s) never ran')



#! Same code as above except noted out and some '>' and '<' were changed
# Remove the note and run it
'''
x = 5
y = 10
z = 22

if x > y: # IT IS NOT
    print('x is greater than y') 
elif x == z: # IT IS
    print('x is less than z') # SO THIS IS RAN
# Since the above 'elif' statement is ran it breaks/stops the rest of the code from being ran
# Once an 'elif' finds something thats true it wont keep searching
elif 5 == 2:
    print('5 is greater than 2')
else:
    print('if an elif never ran')
'''




#! QUESTION
# What will the output be?
#! Don't run this code until you think you have the answer
'''
if 1 > 2 > 3:
    print('#1')
elif 3 > 2 > 1:
    print('#2')
if 1 < 3:
    print('#3')
'''

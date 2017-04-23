## M/D/Y 04/23/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1
#! Errors are included, ignore them until you reach that part in the lesson
# 'CRTL+C' ends a currently running program
# Play around with this code and break it and see why it is broken to help understand the functions
'''
A while loop is used to preform an operation
while the condition is whatever you set
'''

# 'condition' is a variable with the value we assigned as '1'
condition = 1


# The '<' is an assignment operator, this will be convered more in another video
# The while loop is often used as a counter
while condition < 42:
    #! Notice we are tabbed over, the above line ends with ':, colon' this !always? indicates a tab over in the next line
    print(condition)    

    # What '+=' does here is takes the variable adds '1'
    # The '+=' is preforming the action 'condition = condition + 1' just cleaner and with less text
    # If you just typed 'condition + 1' it would tell the program that condition is equal to 1 again and again
    condition += 1
    # The program stops printing at '41' not '42' this is because 42 is not less than 42
    # If you want to print the final number try adding a new 'print()' function to this code

    #print(condition)


'''
The below section has been put into a note to stop the program from going crazy until I get there
'''

'''
# This makes what is known as an infinite loop
# Remember 'CRTL+C' to break or stop the program, sometimes it doesn't instantly shut down the program
while True:
    print('doing stuff')
'''
print('BREAK')
print('BREAK')

ageOfMe = 23

while ageOfMe < 42:
    print(ageOfMe)
    ageOfMe += 1
    print(ageOfMe)

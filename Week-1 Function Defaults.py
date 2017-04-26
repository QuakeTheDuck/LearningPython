## M/D/Y 04/25/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1

#! help() function
'''
"pass" is a null operation --- when it is executed, nothing happens
It is useful as a placeholder when a statement is required
syntactically, but no code needs to be executed, for example:
def f(arg): pass    # a function that does nothing (yet)
'''

def simple(num1,num2):
    pass

def simple(num1,num2=5):
    print(num1,num2)



# Make long parameter lists look cleaner and follow 'PEP 8'
# After the ',' hit enter
def basic_window(width,height,font='TNR',
                 bgc='w',scrollbar=True): # 'bgc' = background colour # YES I AM CANADIAN eh
    print(width,height,font,bgc)
# above we defined the 'bgc' as 'w' which is terrible for a website, its wingdings
# It is changed when we call the parameter belo
print('    easy as')
# Since the other parametes inside the function have been defined
# I need need to give two of the remaining parameters data
basic_window(500,350,bgc='a')
basic_window(500,350,bgc='b')
basic_window(500,350,bgc='c')


#quote
'''
Luckily, we allow people who want to customize their car the option to do it,
but we do not ask every buyer of every car what kind of wheels they want,
what brand of tire, what screws they want, what kind of leather seats by what brand, what windshield,
what steering wheel, what lights... etc.
This is just too much for some people and what they want to use the car for. Same goes for functions in programming
'''


print('1','2','3')

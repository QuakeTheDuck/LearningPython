## M/D/Y 04/28/2017
## Disclaimer: These are all personal notes. +=1 member - Thank you sentdex
## Python 3.6.1


text = 'Sample Text to Save\nNew line!'

# notifies Python that you are opening this file, with the intention to write
saveFile = open('exampleFile.txt','w')

# actually writes the information
saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()


readMe = open('exampleFile.txt','r').readlines() # .readlines() instead of .read
# This will instead create a python list

print(readMe)


help()


'''
# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get:
readMe = open('exampleFile.txt','r').read()
print(readMe)
'''

'''
# this will instead read the file into a python list. 
readMe = open('exampleFile.txt','r').readlines()
print(readMe)
'''

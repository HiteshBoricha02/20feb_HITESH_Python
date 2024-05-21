# Write a Python program to copy the contents of a file to another file.

import os



os.chdir('Assignments/Module-4')


file = open('Assignment.txt','r')

d = file.read()

file1 = open('example.txt','w')

file1.write(d)
print("File Copy successFully...")
file.close()
file1.close()

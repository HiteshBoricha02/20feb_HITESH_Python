# Write a Python program to read a file line by line and store it into a list

import os

os.chdir('Assignments/Module-4')

file_list = [] 
    
file = open('Assignment.txt','r') 
for i in range(2):
        line = file.readline()
        file_list.append(line)

print(file_list)
    

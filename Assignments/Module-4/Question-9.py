# Write a Python program to count the number of lines in a text file.

import os


os.chdir('Assignments/Module-4')

file = open('Assignment.txt')

Assign = len(file.readlines())

print(f"{Assign} in Your File.")
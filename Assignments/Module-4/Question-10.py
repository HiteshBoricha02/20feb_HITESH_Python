# Write a Python program to count the frequency of words in a file.

import os

os.chdir('Assignments/Module-4')

file = open('Assignment.txt')
count = 1
w = input("Enter word You have find: ")
if w in file.read():
    count+=1
    print(f"{w} is {count} times in File.")
    
else:
    print("no word Found in the File.")
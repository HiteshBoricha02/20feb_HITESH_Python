# Write a Python program to read first n lines of a file.



import os

os.chdir('Assignments\Module-4')

file= open('Assignment.txt','r')

n = int(input("Enter lines You have read :"))

read = file.readlines()

for i in read[-n : ]:
    print(i)

file.close()

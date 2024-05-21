

# • Write a Python program to read a file line by line store it into a variable.




import os

os.chdir('Assignments/Module-4')

con = ''

file = open('Assignment.txt','r') 

for i in range(10):

        con += file.readline()

print(con)
    

    
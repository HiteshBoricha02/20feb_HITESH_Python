# Write a Python program to write a list to a file.


import os
os.chdir('Assignments/Module-4')

value = int(input("how many entry you enter :  "))
items = []
for i in range(value):
    
    items.append(input("Enter append entry : "))


file = open('Assignment.txt','w')

for i in items:
    
    file.write(i)
    file.write('\n')
    

file.close()



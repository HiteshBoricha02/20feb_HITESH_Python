

# What is File function in python? What is keywords to create and write file.

import os

print('''
      
      file handling is a crucial operation that allows you to create, read, update, and delete files. 
      The built-in open() function is primarily used for these operations''')

os.chdir('Assignments\Module-4')
 
file = open("Assignment.txt", "w")

file.write("Hello, This Is a Python File Handling\n")
file.write("This is a new file created and written in Python.\n")
    
    



file.close()

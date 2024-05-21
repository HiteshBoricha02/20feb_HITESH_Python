# Write a Python program to append text to a file and display the text.

 

import os
os.chdir('Assignments\Module-4')
append = 'Hello I am Hitesh Boricha'
with open('Assignment.txt', 'a') as file:
        file.write(append + '\n')
    
    
with open('Assignment.txt', 'r') as file:
        content = file.read()
        print("edited  File:")
        print(content)


file = 'example.txt'




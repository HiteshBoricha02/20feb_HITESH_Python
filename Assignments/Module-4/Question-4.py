
# • Write a Python program to read first n lines of a file.


import os
   
n = int(input("Enter The lines you have read :"))
os.chdir('Assignments\Module-4')
with open('Assignment.txt', 'r') as file:
            
            for i in range(n):
                
                line = file.readline()
                
                if not line:
                    break
            
                print(line, end='')
    
   
            




 

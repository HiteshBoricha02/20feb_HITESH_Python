# Write a Python program to read an entire text file.

 
def file(file_path):
    
    
        with open(file_path, 'r') as file:
        
            content = file.read()
            
            print(content)
    
    

file_path = 'example.txt'


file(file_path)

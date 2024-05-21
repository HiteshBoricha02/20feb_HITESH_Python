

# • Write a Python program to read a file line by line store it into a variable.


def read_variable(path):
    
        
        content = ""
        
        
        with open(path, 'r') as file:
            
            for line in file:
                content += line  
        
        return content
    
   


path = 'example.txt'


content = read_variable(path)


print(content)

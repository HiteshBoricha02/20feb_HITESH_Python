# Write a Python program to read a file line by line and store it into a list


def file(path):
    
        
        lines = []
        with open(path, 'r') as file:
            
            for line in file:
                lines.append(line.strip())  
        
        return lines
    
path = 'example.txt'
line = file(path)
print(line)

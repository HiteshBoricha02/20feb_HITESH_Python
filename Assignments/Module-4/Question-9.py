# Write a Python program to count the number of lines in a text file.

def count_lines(path):
        with open(path, 'r') as file:
            count = 0
            for line in file:
                count += 1
        
        return count

path = 'example.txt'  
lines = count_lines(path)
if lines != -1:
    print(f"Number of lines in '{path}': {lines}")

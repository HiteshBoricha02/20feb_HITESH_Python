

from collections import deque


def read_lines(file_path, n):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            
            last_n_lines = deque(file, maxlen=n)
        
        # Print the last n lines
        for line in last_n_lines:
            print(line, end='')
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error: {e}")

file_path = 'example.txt'
n = int(input("Enter The line Number :"))

# Call the function 
read_lines(file_path, n)

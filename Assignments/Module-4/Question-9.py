# Write a Python program to count the number of lines in a text file.

def count_lines(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            
            line_count = 0
            
            
            for line in file:
                
                line_count += 1
        
        return line_count
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1


file_path = 'example.txt'  


num_lines = count_lines(file_path)


if num_lines != -1:
    print(f"Number of lines in '{file_path}': {num_lines}")

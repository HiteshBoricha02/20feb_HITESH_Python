# Write a Python program to read a file line by line and store it into a list


def file_to_list(file_path):
    try:
        
        lines = []
        
        # Open the file in read mode
        with open(file_path, 'r') as file:
            
            for line in file:
                lines.append(line.strip())  
        
        return lines
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_path = 'example.txt'

# Call the function 
lines_list = file_to_list(file_path)

# Print the list
print(lines_list)

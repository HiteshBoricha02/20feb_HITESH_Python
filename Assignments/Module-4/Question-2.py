# Write a Python program to read an entire text file.

 
def read_entire_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file
            content = file.read()
            # Print the content
            print(content)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# file path
file_path = 'example.txt'

# Call the function to read the file
read_entire_file(file_path)

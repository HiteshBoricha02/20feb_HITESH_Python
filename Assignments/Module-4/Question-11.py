# Write a Python program to write a list to a file

def write_file(file_path, my_list):
    try:
        
        with open(file_path, 'w') as file:
            
            for item in my_list:
                file.write(str(item) + '\n')
        
        print(f"List has been written to {file_path} successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'example.txt'

my_list = ['apple', 'banana', 'cherry', 'date', 'year']


write_file(file_path, my_list)

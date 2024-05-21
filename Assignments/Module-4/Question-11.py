# Write a Python program to write a list to a file

def file(file_path, my_list):
   
        with open(file_path, 'w') as file:
            
            for item in my_list:
                file.write(str(item) + '\n')
        
        print(f"List  written  {file_path} successfully.")
    
    


path = 'example.txt'

list = ['apple', 'banana', 'cherry', 'date', 'year']


file(path, list)

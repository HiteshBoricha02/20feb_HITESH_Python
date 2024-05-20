

# • Write a Python program to read a file line by line store it into a variable.


def read_variable(file_path):
    try:
        
        file_content = ""
        
        
        with open(file_path, 'r') as file:
            
            for line in file:
                file_content += line  
        
        return file_content
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return ""
    except Exception as e:
        print(f"An error : {e}")
        return ""


file_path = 'example.txt'


file_content = read_variable(file_path)


print(file_content)

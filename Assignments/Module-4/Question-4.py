
# • Write a Python program to read first n lines of a file.


def read_lines(file_path, n):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            
            for i in range(n+1):
                
                line = file.readline()
                
                if not line:
                    break
            
                print(line, end='')
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'example.txt'
n = int(input("Enter The lines you have read :"))

# Call the function 
read_lines(file_path, n)

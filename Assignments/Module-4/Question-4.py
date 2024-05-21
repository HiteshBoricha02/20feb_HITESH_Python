
# • Write a Python program to read first n lines of a file.


def read_file(path, n):
   
        with open(path, 'r') as file:
            
            for i in range(n+1):
                
                line = file.readline()
                
                if not line:
                    break
            
                print(line, end='')
    
   
        print(f"error in the file: ")


file_path = 'example.txt'
n = int(input("Enter The lines you have read :"))

 
read_file(file_path, n)

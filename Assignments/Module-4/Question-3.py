# Write a Python program to append text to a file and display the text.

 
def fille_opction(file1,append):
    
    with open(file1, 'a') as file:
        file.write(append + '\n')
    
    
    with open(file1, 'r') as file:
        content = file.read()
        print("edited  File:")
        print(content)


file = 'example.txt'
append = 'Hello I am Hitesh Boricha'


fille_opction(file,append)

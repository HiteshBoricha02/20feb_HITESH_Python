# Write a Python program to append text to a file and display the text.

 
def display(file_path, text_to_append):
    # Append text to the file
    with open(file_path, 'a') as file:
        file.write(text_to_append + '\n')
    
    
    with open(file_path, 'r') as file:
        content = file.read()
        print("Updated File:")
        print(content)


file_path = 'example.txt'
text_to_append = 'This is the appended text.'

# Call the function
display(file_path, text_to_append)

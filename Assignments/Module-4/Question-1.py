

# What is File function in python? What is keywords to create and write file.



print('''
      
      file handling is a crucial operation that allows you to create, read, update, and delete files. 
      The built-in open() function is primarily used for these operations''')


# Open a file 
file = open("example.txt", "w")

# Write some text to the file
try:
    file.write("Hello, This Is a Python File Handling\n")
    file.write("This is a new file created and written in Python.\n")
    
    
except Exception as e:
    print(e)


# close the file 
file.close()

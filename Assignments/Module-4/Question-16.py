

# • Can one block of except statements handle multiple exception?

print('''
      Yes, a single except block can handle multiple exceptions. In Python, 
      you can specify multiple exceptions in a single except clause by providing a tuple of exception types. 
      This allows you to handle several types of exceptions with the same block of code.
      ''')

def division():
    try:
        
        num = int(input("Enter a number: "))
        
        
        result = 10 / num
        
    except (ValueError, ZeroDivisionError) as e:
        
        print(f" error in your input : {e}")
    
    else:
       
        print(f" result is: {result}")
    
    finally:
        
        print(" block is complete.")

# Call the function
division()

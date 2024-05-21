# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets.

def division(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except :
        print(f"Error: Cannot divide by zero!")
    
    finally:
        print("Execution of the try-except block is complete.")


a = int(input("Enter The Value of a :"))
b =int(input("Enter The Value of b :"))


division(a,b)
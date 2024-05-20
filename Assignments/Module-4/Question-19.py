# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets.

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero! ({e})")
    except TypeError as e:
        print(f"Error: Invalid input type! ({e})")
    else:
        print("Division was successful without any errors.")
    finally:
        print("Execution of the try-except block is complete.")


a = int(input("Enter The Value of a :"))
b =int(input("Enter The Value of b :"))


divide_numbers(a,b)
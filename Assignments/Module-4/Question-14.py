# How many except statements can a try-except block have? Name Some
# built-in exception classes:


try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = 1 / num2
    print(f"Result: {result}")

except ValueError:
    
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    
    print("Division by zero is not allowed!")

except Exception as e:
    
    print(f"An unexpected error occurred: {e}")


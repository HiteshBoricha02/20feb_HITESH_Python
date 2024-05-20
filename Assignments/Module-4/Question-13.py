# • Explain Exception handling? What is an Error in Python?

try:
    
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The second Number :"))
    result = num1 / num2
    print(f"Result: {result}")

except ValueError:
    
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    
    print("Division by zero is not allowed!")

finally:
    
    print("try-except block is complete.")
    
    
    

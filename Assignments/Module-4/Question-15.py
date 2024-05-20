
# When will the else part of try-except-else be executed?

try:
    num1 = int(input("Enter a number: ")) 
    num2 = int(input("Enter a number: "))  
    result = num1 / num2  
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
   
    print(f"The result is: {result}")
finally:
    
    print("Execution of the try-except-else block is complete.")

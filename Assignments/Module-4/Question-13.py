# • Explain Exception handling? What is an Error in Python?

print("""
        - Errors is the problem due to that our program get's terminated before its completion.\n
        - Exception Handling is nothing but runtime errors and it occurs due to incorrect logics.
        - when error occurs instead of terminating program we can move to the next process with the help of exception.    
        - eg. when we try to divide any numbers with zero or we are importing something that is not available.
      """)

try:
    
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The second Number :"))
    result = num1 / num2
    print(f"Result: {result}")

except:
    
    print("error pleas Enter A Valid Input ......")




    
    
    

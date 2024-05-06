# Write a Python function to calculate the factorial of a number (a nonnegative integer) 



num = int(input("Enter Number to Find Factorial : "))

def factorial(value):
    
    fact = 1
    
    if (value < 0):
        print("-- Enter Positive Number --")
    
    elif(value >= 0):
        
        for i in range(1,value+1):
            
            fact *= i 
        print(f"Factorial of {value} is : {fact}")
        
factorial(num)
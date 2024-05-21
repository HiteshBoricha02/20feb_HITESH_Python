
# When will the else part of try-except-else be executed?

try:
    num1 = int(input("Enter a number: ")) 
    num2 = int(input("Enter a number: "))  
    result = num1 / num2  

except :
    print("Error enter valid input")
else:
   
    print(f"The result is: {result}")



# When will the else part of try-except-else be executed?

print('''   In Try-Except-Else else part will be executed if try part will get execute without any exception.
          - If any Exception occurs then else part will be not executed.''')

try:
    num1 = int(input("Enter a number: ")) 
    num2 = int(input("Enter a number: "))  
    result = num1 / num2  

except :
    print("Error enter valid input")
else:
   
    print(f"The result is: {result}")
    


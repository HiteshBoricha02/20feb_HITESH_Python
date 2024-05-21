# How many except statements can a try-except block have? Name Some
# built-in exception classes:

print("\n==== How many except statements can a try-except block have? ===\n")

print("- Try Except block must have at least one except statement.")
print("- We can also apply more then one except statement.\n\n")



print('''=== Name Some built-in exception classes ===\n
 List of Exception Classes : 
 Zero Division Error - number can not be divided by zero
 Index Error - occurred When given index is wrong  
 Key Error - occurred when given key of dictionary is not declared or wrong
 Value Error - when type of value is not same as assigned type
 Name Error - when variable is not declared and we use it ''')


try:
   
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = 1 / num2
    print(f"Result: {result}")

except :
    
    print("Invalid input! Please enter a valid number.")
    






# When is the finally block executed?


# When is the finally block executed?



print("Finally Block Executed in the end even try block has occurred with exception or without exception.")

try:
    a = input("Enter Value of a :")
    b = int(input("Enter The Value of b :"))
    
    c = a+b

except (NameError, TypeError) as error:
    print(error)

else:
    print(c)

    


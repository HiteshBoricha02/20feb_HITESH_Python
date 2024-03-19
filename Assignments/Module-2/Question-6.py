# Write python program that swap two number with temp variable and
# without temp variable

A = int(input("Enter First Number :"))
B = int(input("Enter Second Number :"))

print("Before Swapping Value of A :",A)
print("Before Swapping Value of B :",B)

Choice = input("Enter Your Choice With Or Without :")
if(Choice == "With" or Choice == "Without"):
    if(Choice == "With"):
        C = A
        A = B
        B = C
        print("-----------------With Tamp variable Swapping------------------- ")
        print("With Tamp Variable Swapping Value of A :",A)
        print("With Tamp Variable Swapping Value of B :",B)
    if(Choice == "Without"):
        A,B = B,A 
        print("-----------------Without Tamp variable Swapping------------------- ")
        print("Without Tamp Variable Swapping Value of A :",A)
        print("Without Tamp Variable Swapping Value of B :",B)
else:
    print("Please Enter Valid Choice :")
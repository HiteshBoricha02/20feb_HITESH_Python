# Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

Num1 = int(input("Enter Num1 :"))
Num2 = int(input("Enter Num2 :"))
Num3 = int(input("Enter Num3 :"))

if(Num1==Num2 or Num1==Num3 or Num2==Num3):
    print("Sum is Zero Two value Are Equal")
else:
    sum = Num1+Num2+Num3
    print("Sum of Three Number is :",sum)

# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

Num1 = int(input("Enter Num1 :"))
Num2 = int(input("Enter Num2 :"))

if(Num1==Num2 or Num1-Num2 == 5 or Num1+Num2 == 5):
    print("True")
   
else:
    print("False")
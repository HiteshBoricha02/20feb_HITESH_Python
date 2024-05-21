# • Write python program that user to enter only odd numbers, else will
# raise an exception.

number = int(input("Enter The number  : "))

try:
    if number%2==0:
        print("Number is Even Number....")
        
except:
    print("please Enter only Odd Numbers.... ")


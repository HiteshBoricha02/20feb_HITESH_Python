# Write a Python program to check whether an element exists within a
# tuple

tuple=(1,2,3,4,5,6,7)
num = int(input("Enter You are find Number :"))

if num in tuple:
    print(f'{num} is in tuple')
    print(tuple)
else:
    print(f"{num}is Not in tuple")
    print(tuple)


# Write a Python program to get the Fibonacci series of given range.


num = int(input("Enter The Number :"))

n1 = 0
n2 = 1 
for i in range(num):
    print(n1)
    
    n3 = n1 + n2
    n1 = n2
    n2 = n3 

# Write a python program to sum of the first n positive integers.

n = int(input("Enter The Number :"))
j = 0

for i in range(1,n+1):
    j +=i
    
    
print("Sum of N is:",j)
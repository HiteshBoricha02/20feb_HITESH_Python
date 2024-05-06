# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.

al = [i**2 for i in range(1,31)]
print(al)
print("first five number square is...",al[:5])
print("last five Number square is...",al[-5:])
# Write a Python program to print all unique values in a dictionary. 



numbers = []
unique = {}
key = 1
value = int(input("Enter an number of Entries : "))

for i in range(1,value+1):
    numbers.append(input(f"Enter {i} Value : "))
    
for i in numbers:
    
    if i not in unique.values():
        unique[key] = i
        key += 1


print(f"Dictionary with unique Values : {unique}")
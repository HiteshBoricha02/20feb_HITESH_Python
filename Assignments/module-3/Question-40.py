# Write a Python program to map two lists into a dictionary 



l1 = [1,2,3,4,5]

l2 = ['a', 'b', 'c', 'd', 'e']

dictionary = {}

for i in range(len(l1)):
    
    dictionary[l1[i]] = l2[i]
    
print(f"First List : {l1}")
print(f"Second List : {l2}")

print(f"Dictionary after Mapping two List : {dictionary}")
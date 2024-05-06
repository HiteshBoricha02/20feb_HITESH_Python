# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource' 


string = 'w3resource'

dictionary = {}
count = 1

for i in string:
    
    key = i
    if key not in dictionary:
        dictionary[key] = count
    else:
        dictionary[key] +=count
        
print(dictionary)
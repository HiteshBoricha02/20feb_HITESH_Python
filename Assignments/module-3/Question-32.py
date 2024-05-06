# Write a Python script to concatenate following dictionaries to create a
# new one.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

 
concatenated_dict = {**dict1, **dict2, **dict3}


print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
print("Concatenated Dictionary:", concatenated_dict)
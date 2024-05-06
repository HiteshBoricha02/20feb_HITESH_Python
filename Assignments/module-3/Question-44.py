# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']} 

print("\n--- This Program is return every combinations of a different keys ---\n\n")

numbers = {'1' : ['a','b'] , 
           '2' : ['c','d']}

for i in numbers['1']:

    for j in numbers['2']:
        
        print(i+j)

    print(i+i)
    
    
# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']} 

numbers = {'Hitesh' : ['a','b'] , 
           'Mihir' : ['c','d']}

for i in numbers['Hitesh']:

    for j in numbers['Mihir']:
        
        print(i+j)

    print(i+i)
    
    
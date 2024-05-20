# Write a Python script to check if a given key already exists in a dictionary.



subjects = {1: 'HTML', 2: 'CSS', 3: 'JS', 4: 'BootStrap', 5: 'jQuery', 6: 'C', 7: 'C++', 8: 'MySQL', 9: 'Python', 10: 'Django'}

# input for enter key for find values
word = int(input("Enter Key to find Values : ")) 

if word in subjects.keys():
    
    print(f"{word} : {subjects[word]}")
    
else :
    print("Not Found the matching key")
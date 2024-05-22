# How Do You Check The Presence Of A Key In A Dictionary? 



library = {1 : 'A',
           2 : 'B',
           3 : 'C',
           4 : 'D',
           5 : 'E',}

print(f"Dictionary : {library}")



find  = int(input("Enter a key and check key is exist or not : "))

if find in library.keys():
    print(f"{find} key is Exist You have find")
    print(library[find])

else:
    print(f"{find} key is not exist in this name...")

 
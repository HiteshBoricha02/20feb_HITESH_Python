# How Do You Check The Presence Of A Key In A Dictionary? 



library = {1 : 'html',
           2 : 'css',
           3 : 'js',
           4 : 'Book4',
           5 : 'Book5',}

print(f"Dictionary : {library}")



find  = int(input("Enter a key is exist or not : "))

if find in library.keys():
    print(f"{find} Exists")
    print(library[find])

else:
    print(f"{find} Doesn't Exists...")

 
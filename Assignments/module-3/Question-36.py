# How Do You Check The Presence Of A Key In A Dictionary? 



library = {1 : 'Book1',
           2 : 'Book2',
           3 : 'Book3',
           4 : 'Book4',
           5 : 'Book5',}

print(f"Dictionary : {library}")


print("\nKey are integer so enter Numeric Value")
find  = int(input("Enter an Key to find it exists or not : "))

if find in library.keys():
    print(f"{find} Exists")
    print(library[find])

else:
    print(f"{find} Doesn't Exists...")

 
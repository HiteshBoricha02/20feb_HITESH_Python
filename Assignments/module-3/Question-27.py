# Write a Python program to remove an empty tuple(s) from a list of tuples.

list1 = [(1,2,3),(),("hitesh"),("Mihir"),(),(3,5,7)]

for i in list1:
    if i == ():
        list1.remove(())
print(list1)
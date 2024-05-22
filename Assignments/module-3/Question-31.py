# How will you create a dictionary using tuples in python? 

value = int(input("Enter Values for Tuple : "))

list1= []
list2 = [] 

for i in range(1,value+1):
    list1.append(input(f"Enter {i} key: ")) 
    list2.append(input(f"Enter {i} Value : ")) 

tuple1 = tuple(list1)
tuple2 = tuple(list2)

dict = {}

for i in range(value):
    
    dict[list1[i]] = list2[i] 

print(dict)

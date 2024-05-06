# Write a Python function that takes two lists and returns true if they have
# at least one common member.

def fun(list1,list2):
   common = set(list1) &set (list2) 
   return common

list_1 = [1,2,3,4,5]
list_2 = [5,6,7,8]

if fun(list_1,list_2):
    print("list Have last one common...",True)
else:
    print("List have no any common numbers....",False)
    
    
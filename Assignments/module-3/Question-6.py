# • Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings

val = int(input("Enter how many value You entered :"))
list = []
same = []
for i in range(val):
    str1=input("Enter The String :")
    
    list.append(str1)
    if(str1[0]==str1[-1]):
        same.append(str1)
        
    
print(list)
print(str(same))
print(type(same))
# • Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

str1 = input("Enter Your Name :")
str2= input("Enter Your Surname :")
a = str1[0]
b = str1[1]
a,b = b,a

c = str2[0]
d = str2[1]
c,d = d,c
print(a,b,str1[2:])

print(a+b+str1[2:],'',c+d+str2[2:])


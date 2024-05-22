# Write a Python program to check multiple keys exists in a dictionary  


student = {}

entries = int(input("Enter number of entries : "))

for i in range(1,entries+1):
    key = input("Enter Key : ")
    value = input("Enter value : ")
    student[key] = value
     
keyList = []

for i in student.keys():
    keyList.append(i)
        
if ( len(keyList) < 2):

    
    print("No...This Dictionary has less then 2 keys")
    
else:
   
    print("Yeh....Your Dictionary has Multiple keys.")
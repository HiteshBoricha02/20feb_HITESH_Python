

tops = {}

k = int(input("Enter The Numbers of Key :"))


for i in range(k):
    
    dict_name=input("Enter Your Dict Name :")
    tops[dict_name]={}
    
    name = input("Enter Your Name :")
    city = input("Enter Your City :")
    
    tops[dict_name]["Name"]=name
    tops[dict_name]["City"]=city
    
print(tops)
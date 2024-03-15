
#  Get user Name From input
Name = input("Enter Your Name :")
if (Name.isalpha()):
    print(Name)
    # Get Age from User Input
    Age = input("Enter Your Age :")
    if (Age.isdigit()):
        print(Age)
    else:
        print("Enter Valid Age")
        
        # Get Email For User Input
    Email = input("Enter Your Email :")
    if(Email.islower()):
        print(Email)
    else:
        print("please Enter Valid Email ")
        
        
        # Password for user input 
    pas = input("Enter YOur Pass :")
    if(pas.isalnum()):
       
        # For Conform Password
        c_pas = input("Enter Your C pass")  
        if(c_pas == pas):
           print(pas)
        else:
          print("Your Password Is not Match")
        
    else:
        print("Enter Valid Password")
        
        
    
else:
    print("please Enter Valid Name")    
        
        
    
    
    
print("-----------------------------Registration Success--------------------------------")
print("---------------------------",Name,"Welcome TO my website -------------------------------")

print("Your Name is :",Name)
print("----------------")
print("Your Age is :",Age)
print("----------------")
print("Your Email is :",Email)
print("----------------")
print("Your pass is :",pas)

        
    
   
    
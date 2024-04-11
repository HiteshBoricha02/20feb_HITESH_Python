import random

def detail():
    global bal
    Name = input("Enter Account Holder Name :")
    Account_number = random.randrange(1111111111,9999999999)
    Number = int(input("Enter The Number :"))
    bal= 1000
    print("<<<=============Details=============>>>")
    print("Name :",Name)
    print("Account Number :",Account_number)
    print("Number :",Number)
    
detail()
    
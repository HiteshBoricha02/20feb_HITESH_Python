import Create

def withdraw():
    amount = int(input("Enter Your Withdraw Amount :"))
    if(amount>=Create.bal):
        print("Please inter Valid Amount")
    else:
        print("Withdraw Success",Create.bal)
        
withdraw()
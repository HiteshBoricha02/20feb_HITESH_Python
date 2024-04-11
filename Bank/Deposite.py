
import Create

def dep():
    deposit = int(input("Enter A deposit Amount :"))
    
    if(deposit>2000):
        print("Deposit Success",deposit)
    else:
        print("Sorry Not Deposit Minimum Deposit is 2000")
        
dep()
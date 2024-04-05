

# Bank Management system using function


# AC_NO = int(input("Enter ACount NUmber :"))
# NAME = input("Enter Your Name :")
# AC_TYPE = input("Enter Your Acount Type Saving/ Current :")
BAL = int(input("Enter Your Bal :"))
    
def CREATE():
    # print("ACCOUNT NO :",AC_NO)
    # print("NAME :",NAME)
    # print("ACCOUNT TYPE :",AC_TYPE)
    print("BALANCE :",BAL)


def deposit():
    global BAL
    Ammount = int(input("Enter Amount :"))
    
    if(Ammount< 2000):
        print("Deposit Amount is more Than 2000 ")
    else:
        BAL = BAL + Ammount
        print(f"{Ammount} ADD IN YOUR ACCOUNT ")

def width():
    global BAL
    amount1= int(input("Enter Withdrow Amount"))
    
    if(amount1 > BAL):
        print("REQUEST IS MORE THAN BAL")
    else:
        BAL = BAL - amount1
        print(f"{amount1} WITHDRAW  IN YOUR ACCOUNT ")
        
def statement():
    CREATE()
    
    
# -----------------------
print("Enter Deposit For Deposit")
print("Enter Withdraw for Withdraw")
print("Enter Statement for statement")

Choice = input("Enter Your Choice :")

if (Choice=="deposit"):
    deposit()
elif(Choice=="Withdraw"):
    width()
elif(Choice=="Statement"):
    statement()
else:
    print("Enter The Valid Choice")


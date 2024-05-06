
# create bank management system using inheritance
import random

class details:
    name = ""
    ac_no = random.randint(111111,999999)
    bal = 0
    ac_type = ""
    
    def get_detail(self):
      self.name = input("Enter Your Name :")
      self.bal = input("Enter Your Bal :")
      self.ac_type = input("Enter Your Account Type :")
      
class deposit(details):
      dep = 0
      def deposit(self):
          self.dep = input("Enter Deposit Amount :")
          if(self.dep>=2000):
              self.dep+=self.bal
              print("Amount Add success----",self.bal)
          else:
              print("Enter The Valid Amount ----")
              
class withdraw(details):
    wid = 0
    def wid(self):
        self.wid = input("Enter Withdraw Amount")
        
        if (self.wid>self.bal):
            print("Enter Small Amount Than Bal")
        else:
            self.bal-=self.bal
            print(self.bal)

class statement(details):
    
    def state_ment(self):
        print("Account Holder Name :",self.name)
        print("Account Number Is :",self.ac_no)
        print("Account Type is  :",self.ac_type)
        
detail = details()
depo = deposit()
wit = withdraw()
state = statement()
            
    
        
    
    
    
    
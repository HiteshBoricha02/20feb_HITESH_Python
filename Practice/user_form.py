# polymorphism

class adding:
    def Addition(self,a,b):
        
        print("a + b :",a+b)
    
    def sub(self,a,b):
        
        print("a - B :",a-b)
    
    def mul(self,a,b):
        print("a * b :",a*b)
        
        
    
    def div(self,a,b):
        print("a / b :",a/b)
    
class addition(adding):
    def Addition(self, a, b):
        return super().Addition(a, b)

class subtraction(adding):
    def sub(self, a, b):
        return super().sub(a, b) 
    
class multiplication(adding):
    def mul(self, a, b):
        return super().mul(a, b)
    
    
class division(adding):  
    def divs(self, a, b):
        return super().div(a, b)
    
    
ad = adding()
sb = subtraction()
ml = multiplication()
dv = division()

a = int(input("Enter The value of a :"))
b = int(input("Enter The VAlue of b :"))

ad.Addition(a,b)
sb.sub(a,b)
ml.mul(a,b)
dv.divs(a,b)

    
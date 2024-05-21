# Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?


print('''Inheritance :
        Inheritance is a fundamental concept in object-oriented programming (OOP) where a new class (child or subclass) is created based on an existing class 
        (parent or superclass). The child class inherits attributes and methods from the parent class, ''')

print("Example :")


class ops:
    a :int
    b: int
    def __init__(self) :
        self.a = int(input("Enter First Value : "))
        self.b = int(input("Enter Second Value : "))
        
        
class Sum(ops):
    
    def __init__(self):
        
        super().__init__()
        
        c = self.a + self.b
        
        print(f"Sum of {self.a} and {self.b} is : {c}")

add = Sum() 

  
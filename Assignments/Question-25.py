# Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?


print('''Inheritance :
        Inheritance is a fundamental concept in object-oriented programming (OOP) where a new class (child or subclass) is created based on an existing class 
        (parent or superclass). The child class inherits attributes and methods from the parent class, ''')

print("Example :")


class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name}  Woof woof"


class Cat(Animal):
    def speak(self):
        return f"{self.name}  Meow meow"

dog_name = input("Enter Dog  Name :")
cat_name = input("Enter Your cat Name :")
dog = Dog(dog_name)
cat = Cat(cat_name)


print(dog.speak())  
print(cat.speak())  



print("Constructor :")

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display_info(self):
        print(f"Name is : {self.name},And my Age is : {self.age}")

name = input("Enter Your Name :")
age = int(input("Enter YOur Age :"))
person = Person(name,age)

person.display_info()  


# How to Define a Class in Python? What Is Self? Give An Example Of
# A Python Class


print("What is class ?")
print("    =>  a class is defined using the class keyword. class is a collection of data member and member function ")

print("What is self ?")
print(" =>   self refers to the instance of the class. It is used to access variables and methods associated with the current object.")


print("Example of class :")

class Person:
    def data(self, name, age):
        self.name = name 
        self.age = age    

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))
person1 = Person()

person1.data(name,age)
person1.greet()

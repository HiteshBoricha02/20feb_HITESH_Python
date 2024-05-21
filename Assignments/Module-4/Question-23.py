# • Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length  
        self.width = width    

    def area(self):
        return self.length * self.width  

length = int(input("Enter The Length :"))
width = int(input("Enter The Width :"))
rect = Rectangle(length,width)
print(f"The area of the rectangle is: {rect.area()}")

# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle


pi = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return pi * (self.radius ** 2)  

    def perimeter(self):
        return 2 * pi * self.radius  

radius = int(input("Enter The radius :"))
circle = Circle(radius)
print(f"The area of the circle is: {circle.area()}")
print(f"The perimeter of the circle is: {circle.perimeter()}")

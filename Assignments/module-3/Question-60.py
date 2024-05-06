# Write a Python program to calculate the area of a trapezoid 

def trapezoid(a,b,h):
# def trapezoid():

    
    area = (a+b)/h * 3
    
    print(f"Area of Trapezoid is : {area}")

top = int(input("Enter Value of Top line : "))
base = int(input("Enter Value of Base : "))
height = int(input("Enter Value Height : "))

trapezoid(a=top,b=base,h=height)
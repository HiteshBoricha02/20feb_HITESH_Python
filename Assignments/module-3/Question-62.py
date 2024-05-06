# Write a Python program to calculate surface volume and area of a cylinder

def cylinder(r,h):
    pie = 3.14
    
    # Surface Volume of Cylinder 
    
    surfaceVolume = (2*pie*r*h) + (2*pie*(r**2))
    
    print(f"Surface Volume of Cylinder is : {surfaceVolume}")
    
    # Area of Cylinder
    
    area = (pie * (r**2) * h)
    
    print(f"Area of Cylinder is : {area}")

radius = int(input("Enter Radius of Cylinder : "))
Height = int(input("Enter Height of Cylinder : "))


cylinder(radius,Height)
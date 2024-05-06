# Write a Python program to calculate the area of a parallelogram

def parallelogram(b,h):
    
    area = b*h
    
    print(f"Area of Your Parallelogram is : {area}")

base = int(input("Enter Value of Parallelogram : "))
height = int(input("Enter Height of Parallelogram :  "))

parallelogram(b = base,h = height)
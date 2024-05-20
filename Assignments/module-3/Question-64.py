# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
 

def min_max():
    
    num = []

    value = int(input("Enter How many number you want to enter : "))

    for i in range(1,value+1):

        num.append(float(input(f"Enter {i} Value : ")))

    max_value = max(num)
    min_value = min(num)

    # Outputting the results
    print("\nMaximum value :", max_value)
    print("Minimum value :", min_value)
    
min_max()
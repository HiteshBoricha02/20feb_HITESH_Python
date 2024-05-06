# Write a Python program to find the highest 3 values in a dictionary

values = int(input("Enter Number of Values : "))

numbers = {}
ch = 64
for i in range(1,values+1): 

    numbers[f'{chr(ch+i)}'] = int(input(f"Enter {i} a Value : "))
    

sorting = sorted(numbers.values())

n1 = sorting[-1]
n2 = sorting[-2]
n3 = sorting[-3]

print(f"Largest Value : {n1}\nSecond Largest Value : {n2}\nThird Largest Value : {n3}")




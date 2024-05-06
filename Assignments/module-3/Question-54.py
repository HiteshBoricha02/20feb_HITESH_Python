# How can you pick a random item from a range? 

import random

numbers = []

sr = int(input("Enter Starting Value of Range : "))
er = int(input("Enter Ending Value of Range : "))

for i in range(sr,er+1):
    numbers.append(i)
    
pick = random.choice(numbers)

print(f"\nRandom Number from {sr} to {er} is : {pick}")

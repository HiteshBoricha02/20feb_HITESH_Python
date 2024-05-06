# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.



student = {}

for i in range(1,16):
    student[i] = input(f"Enter Name Of {i} Student : ")

    
print(f"Your Dictionary : {student}")
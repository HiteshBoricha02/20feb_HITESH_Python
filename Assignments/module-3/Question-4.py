# Write a Python function to get the largest number, smallest num and sum
# of all from a list

def list():
    list1 = [1,3,9,11,90,5,22]
    sum = 0
    list1.sort()
    print("largest Number is :",list1[-1])
    print("small Number is :",list1[0])
    for i in list1:
        sum += i
    print(f"sum of list is :{sum}")

list()
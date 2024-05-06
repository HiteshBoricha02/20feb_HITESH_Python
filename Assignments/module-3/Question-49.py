# Write a Python function to check whether a number is in a given range



number = int(input("Enter an Number you want to find : "))
startRange = int(input("Enter Starting Range Number : "))
endRange = int(input("Enter Stooping Range Number : "))

def find(num,sr,er):

    listt = [] 
    
    for i in range(sr,er):
        listt.append(i)
        
    
    if num in listt:
        print(f"\n{num} is in the Range.")
    else:
        print(f"\n{num} is not in the Range.")
        
        
            

find(num = number,er = endRange,sr = startRange)
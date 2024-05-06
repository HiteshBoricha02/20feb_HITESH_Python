# Write a Python program to returns sum of all divisors of a number 

def divisors(num):
    
    sum = 0
    for i in range(1,num+1):
        
        if (i%num == 0):
           
           sum += i
    print(sum)
    
number = int(input("Enter an Number : ")) 

divisors(number)
            
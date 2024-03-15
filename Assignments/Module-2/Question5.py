
# What is the purpose continue statement in python?

for i in range(0,6):
    for j in range(i):
        if(j==0):
            continue
        print(j,end="")
        
    print("")
    
str = '''In Python, the continue statement is used to skip the rest of the code inside 
         a loop for the current iteration and proceed to the next iteration. It is typically 
         used within loops such as for loops and while loops.'''
         
print(str)

space = 7

for i in range(1,6):
    
    for j in range(0,space):
        print(' ',end='')
    space +=2
        # print
        
    for k in range(5,i-1,-1):
        print(k,end=" ")
    print("")
    
v = 5
for i in range(1,6):
    
    for j in range(space-3,-1,-1):
        print(' ',end='')
    space -=2
        # print
        
    for k in range(i):
        print(v,end=" ")
    v-=1
    print("")
# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} , d2 = {'a': 300, 'b': 200,’d’:400} 


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}

for k,v in d1.items():
     d3[k]= d3.get(k,0) + v
    

for k,v in d2.items():
     d3[k]= d3.get(k,0) + v
     
print(d3)
# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} , d2 = {'a': 300, 'b': 200,’d’:400} 


dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

dict3 = {}

for k,v in dict1.items():
     dict3[k]= dict3.get(k,0) + v
    

for k,v in dict2.items():
     dict3[k]= dict3.get(k,0) + v
     
print(dict3)
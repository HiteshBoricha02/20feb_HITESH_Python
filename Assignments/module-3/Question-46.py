# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},  {'item': 'item1', 'amount': 750}]



SampleData = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},  {'item': 'item1', 'amount': 750}]

temp = {}

for i in SampleData:
    item = i['item']
    amount = i['amount']

    if item not in temp:    
        temp[item] = amount
    
    else:
        temp[item] += amount
        
print(temp)
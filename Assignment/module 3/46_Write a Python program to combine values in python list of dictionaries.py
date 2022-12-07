'''
46_Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
'''
'''
# To find all function in module.
import collections
a = 0
for i in dir(collections) :
    print (f"{a}.collection is :  {i}")
    a +=1
'''
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()

for d in item_list:
    result[d['item']] += d['amount']

print (f"Original items list is : {item_list}")
print (f"output is : {result}") 

'''
a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    

cp={}

val=0

for d in a:
    if d['item'] not in cp:
        cp[d['item']] = d['amount']

print(cp) 
'''
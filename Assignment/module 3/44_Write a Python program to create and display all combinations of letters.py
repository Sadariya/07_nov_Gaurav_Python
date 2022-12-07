'''44_Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}'''

import itertools

dic1 = {'1': ['a','b'], '2': ['c','d']}
x = []

for i in dic1.values():
    x.append(i)

print (f"Original dictionary is : {dic1}")
print (f"\nList of values of dictionary is : {x}")   

print (f"\nOutput is under :-")
for combo in itertools.product(*x):
    print("".join(combo))
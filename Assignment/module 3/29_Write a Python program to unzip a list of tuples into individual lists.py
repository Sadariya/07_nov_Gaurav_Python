# 29_Write a Python program to unzip a list of tuples into individual lists.

# create a list of tuple

l = [(1,2), (3,4), (8,9)]

print (f"Original List :- {l}")

print(f"Zip :- {list(zip(*l))}")
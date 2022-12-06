# 15_Write a Python program to get unique values from a list

# static list :- 
list1 = [1,23,12,16,29,63,29.5,12,16,29]
# print original list :- 
print (f"Original list :- {list1}")

# list to convert into set() :-
x = set (list1)

# print unique values :-
print ("Unique values are : ",end="")
for i in x:
    print (i,end=", ")
# 12_Write a Python program to convert a list of characters into a string.

# Static list :
# list = ['a','b','c','d','e','f']

# User-define list :
list1 = []
n = int(input("Enter the list of items :-"))
for i in range (n):
    list_item = input("Enter the item of list :- ")
    list1.append(list_item)

string = str ()
Length = len (list1)

for i in range (Length) :
    x = list1 [i] 
    string = string + x

print (f"Original list : {list1} \nString is : {string}")
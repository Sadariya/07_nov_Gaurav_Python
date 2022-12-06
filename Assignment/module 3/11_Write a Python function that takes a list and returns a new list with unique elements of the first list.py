# 11_Write a Python function that takes a list and returns a new list with unique elements of the first list.

# User-input list :- 
list_num = []

Number = int(input("Enter the number :- "))

for i in range (Number) :
    number = int (input ("Enter the number to make a list :- "))
    list_num.append (number)

# user-define funciton :- 
def new_list (listno) :
    print (f"Original list : {listno}")
    x = list(set(listno))
    return x

# print New list form list :- 
print (f"newlist : {new_list(list_num)}")
# 28_Write a Python program to remove an empty tuple(s) from a list of tuples.

# static list with empty tuples and tuples
list = [(),("my","Same","Heena"),("Megha","Jatin"),(),(11,12)]
new_list = []

Length = len(list) 

for i in range (Length) :
    if list[i] != ():
        new_list.append(list[i])

print (f"Original list : {list} \n--> New list : {new_list}")
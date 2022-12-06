# 7_Write a Python program to remove duplicates from a list.

list1 = ["Rajkot","Surat","gondal",'simla',"Rajkot"]
print (f"Original list is : {list1}")

# convert list to set because set is not allowed duplicate 
# elements in set 
x = (set(list1))
print (f"Final list is : {list(x)}")

# How Do You Traverse Through A Dictionary Object In Python?
'''
There are multiple ways to iterate over a dictionary in Python.
1_Access key using the build .keys()
2_Access key without using a key()
3_Iterate through all values using .values()
4_Iterate through all key, and value pairs using items()
5_Access both key and value without using items()
6_Print items in Key-Value in pair
'''
# 1_Access key using the build .keys()

dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}

print (f"1.Access key using the key function is  : {dic.keys()}")

# 2_Access key without using a key()

print ("2_Access key without using a key():-")
for i in dic :
    print ("-->",i)

# 3_Iterate through all values using .values()

print (f"3_Iterate through all values using .values() is : {dic.values()}")

# 4_Iterate through all key, and value pairs using items()
print ("4_Iterate through all key, and value pairs using items():-")
for i in dic.items() :
    print ("-->",i)

# 5_Access both key and value without using items()
print (f"5_Access both key and value without using items() :- {dic}")
for i in dic :
    print (i, " --> ", dic[i])

# 6_Print items in Key-Value in pair

keys = dic.items()

print (f"6_Print items in Key-Value in pair :\n--> {keys}")
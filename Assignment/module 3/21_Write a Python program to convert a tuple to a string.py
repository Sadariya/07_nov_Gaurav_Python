# 21_Write a Python program to convert a tuple to a string.

# static tuple
tup = ('het','sam','jack')
str = ""

print (f"Original tuple is : {tup}")

for i in tup :
    str = str + i
    
print (str)
# 21_Write a Python function to reverses a string if its length is a multiple of 4.

# User input string
str = input ("Enter the string name :")

length = len(str)

if length % 4 == 0 :
    length -= 1
    for i in range (length,-1,-1):
        print(str[i],end="")
else :
    print (str)
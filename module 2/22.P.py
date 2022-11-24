# 22_Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.

# User Input
str = input("Enter the string :- ")

#  If the string length is less than 2, return instead of the empty string.
if len(str) < 2 :
    print ("Empty String")
else :
    x = str[:2]
    y = str[-2:]
    
    # Print the final output
    print (f"string is : {x+y}")
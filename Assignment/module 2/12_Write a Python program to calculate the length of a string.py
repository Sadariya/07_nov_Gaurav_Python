# 12_Write a Python program to calculate the length of a string.

# User Input
string = input ("Enter the Full name : ")

# count variable is assign 0 for found length of string using loop
count = 0

# Length of string found using len()
print ("Length of string is ",len(string))

# Length of string found using loop 
for s in string :
    count = count + 1
print ("Length of string is ",count)
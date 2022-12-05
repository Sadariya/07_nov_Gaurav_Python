# 13_Write a Python program to count the number of characters (character frequency) in a string

# User Input
string = input ("Enter the string to count the character in string : ")

# Assign count variable to 0 for count the character
count = 0

# using loop count character but space not count
for i in string :
    if i != " ":
        count = count + 1

# print the count character number
print (count)
# 17_Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

# User Input
str1 = input ("Enter the first string1 :")
str2 = input ("Enter the first string2 :")

# Print 2 strings
print ("String1 : ",str1)
print ("String2 : ",str2)

# print the final string
print ("Final string is :",str1.replace(str1[:2],str2[:2]),end=" ")
print (str2.replace(str2[:2],str1[:2]),end="")
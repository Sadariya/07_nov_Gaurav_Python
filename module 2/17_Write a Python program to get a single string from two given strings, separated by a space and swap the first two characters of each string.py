# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = "Saurav "
str2 = "Gadariya"

print ("String1 : ",str1)
print ("String2 : ",str2)

x = str1[:2]
y = str2[:2]

print ("Final string is :",str1.replace(x,y),end="")
print (str2.replace(y,x))

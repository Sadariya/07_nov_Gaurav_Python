# 2_Write a Python program to get the Factorial number of given number.

# User Input 
Number = int (input ("Enter the number :- "))

# Assign variable for Factorial number.
a = 1 

# Loop is used to count Factorial number of user input.
for i in range (1,Number+1):
    a = a * i

# print Factorial number
print ("Factorial number of",Number,"is",a)
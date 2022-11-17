# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

n1 = int (input ("Enter the 1st number : "))
n2 = int (input ("Enter the 2nd number : "))
n3 = int (input ("Enter the 3rd number : "))

if n1 == n2 or n2 == n3 or n1 == n3:
    sum = 0
else :
    sum = n1 + n2 + n3

print ("Sum of three number is :",sum)
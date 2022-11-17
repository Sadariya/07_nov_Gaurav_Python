# 2.Write a Python program to get the Factorial number of given number.

Number = int (input ("Enter the number :- "))
a = 1 
for i in range (1,Number+1):
    a = a * i
print ("Factorial number of",Number,"is",a)
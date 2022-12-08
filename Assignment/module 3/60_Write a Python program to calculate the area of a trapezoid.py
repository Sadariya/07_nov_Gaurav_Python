'''
60_Write a Python program to calculate the area of a trapezoid
formula :- 
        A = (a + b) /2 * h
'''

a = float (input ("Enter the base value of trapezoid :- "))
b = float (input ("Enter the second base value of trapezoid :- "))
h = float (input ("Enter the height of the trapezoid :- "))

A = (a + b)/2 *h

print (f"Area of trapezoid is : {A}")
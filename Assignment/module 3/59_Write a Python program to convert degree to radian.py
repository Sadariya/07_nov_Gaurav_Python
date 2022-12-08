# 59_Write a Python program to convert degree to radian

import math

# User input degree
degree = float (input("Enter the degree :- "))

# Using deg to rad formul 

radian = degree * (math.pi/180)
print (f"{degree}Deg = {radian}Rad")

# Using radian funciton from math module 

ra = math.radians(degree)
print (f"{degree}Deg = {ra}Rad")
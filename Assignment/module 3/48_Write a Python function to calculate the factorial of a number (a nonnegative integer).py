# 48_Write a Python function to calculate the factorial of a number (a nonnegative integer)

# 1) find Factorial of number using user define function :-
'''
def factorial (number) :
    res = 1
    for i in range (number):
        res = res * (i+1)
    print (f"Factorial of {number} is : {res}")

num = int (input ("Enter the number to find factorial of numbers : "))

factorial (num)
'''
# 2) find Factorial of number using built in module :-
'''
import math 

print (dir(math))
try :
    n = int (input("\nEnter the number :- "))
except :
    print ("Please print valid input ")

print (f"\n-->Factorial number of {n} is : {math.factorial(n)}")
'''

# 3) User-define module--
'''
from my_lib import factorial
print ("To Find Factorial of number :- ")
factorial()
'''
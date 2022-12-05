# 3_Write a Python program to get the Fibonacci series of given range
# a series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers.
# The simplest is the series 0,1, 1, 2, 3, 5, 8, etc.

# User Input
Number = int (input ("Enter the number :- "))

# default value of Fibonacci sequence
default_1 = 0 
default_2 = 1

print ("Fibonacci sequence : ")
print (default_1,end=", ")
print (default_2,end=", ")

# Loop is Used sum of two ahead of number in sequence and
# print also fibinacci sequence till user entered number.
for i in range (Number+1):
    sum = default_1 + default_2
    default_1 = default_2
    default_2 = sum
    if sum <= Number:
        print (sum,end=", ")
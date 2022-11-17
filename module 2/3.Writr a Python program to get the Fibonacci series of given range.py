# a series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers.
# The simplest is the series 0,1, 1, 2, 3, 5, 8, etc.

Number = int (input ("Enter the number :- "))

default_1 = 0 
default_2 = 1

print ("Fibonacci sequence : ")
print (default_1,end=", ")
print (default_2,end=", ")

for i in range (Number+1):
    sum = default_1 + default_2
    default_1 = default_2
    default_2 = sum
    if sum <= Number:
        print (sum,end=", ")
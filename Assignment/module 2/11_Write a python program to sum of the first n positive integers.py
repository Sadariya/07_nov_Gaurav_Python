# 11_Write a python program to sum of the first n positive integers.

# User Input
number = int (input ("Enter the number : "))

# Variable assign 0 to use in loop
a = 0

# if condition is true then sum is done of first n poditive number only
if number > 0 :
    for i in range (number+1):
        if i <= number :
            sum = a + i
            a = sum
    print (f"Sum of positive number is : {sum}")
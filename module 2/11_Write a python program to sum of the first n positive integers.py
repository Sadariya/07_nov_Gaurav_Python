# Write a python program to sum of the first n positive integers.

number = int (input ("Enter the number : "))
a = 0

if number > 0 :
    for i in range (number+1):
        if i <= number :
            sum = a + i
            a = sum
    print (f"Sum of positive number is : {sum}")
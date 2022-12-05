# 7_Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# Loop is Used for 10 time operation of program
for i in range (10):  
# User Input
    Number = int (input ("Enter number to check that number is even or odd : "))
    if Number > 0 :
# If condition is used for check that number is even or odd
        if Number % 2 == 0:
            print ("It is even number.")
        else :
            print ("It is Odd number.")
    else :
        print ("Number is negative.")
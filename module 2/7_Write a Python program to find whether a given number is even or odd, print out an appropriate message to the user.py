# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

for i in range (10):  
    Number = int (input ("Enter number to check that number is even or odd : "))

    if Number % 2 == 0:
        print ("It is even number.")
    else :
        print ("It is Odd number.")
# 1_Write a Python program to check if a number is positive, negative or zero.

# Loop is Used to perform 3 operation of program
for i in range (3):  
# User input :-
    number = int (input("Enter the number : "))

    # if__else and elif with condition .
    if number < 0 :
        print ("Number is Negative.")
    elif number > 0 :
        print ("Number is Positive.")
    else :
        print ("Number is Zero.")
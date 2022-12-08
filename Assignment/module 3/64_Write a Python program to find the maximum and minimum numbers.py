# 64_Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def min_max_decimal (dec_number):

    print (f"All decimal numbers are : {dec_number}")
    print (f"Minimum numbers in decimal number list is : {min(dec_number)}")
    print (f"Maximum numbers in decimal number list is : {max(dec_number)}")


Decimal_number = input("Enter the decimal number : ").split(" ")
    
# Decimal_number = [2.45 ,2.69, 2.45, 231,3.45 ,2.00, 0.04, 7.25,7.26]
min_max_decimal(Decimal_number)
'''
from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))
'''
# 10_Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

# User Input
number1 = float (input ("Enter the first number is :"))
number2 = float (input ("Enter the second number is :"))

# Variable is assign to True 
ans = True

# swapping the number for big number using if condition
if number1 < number2 :
   number1,number2 =number2,number1

# two number of sum and diff is done for result output.
sum = number1 + number2
dif = number1 - number2

# Check condition then print the true and false.
if number1 == number2 or sum == 5 or dif == 5:
   print (ans) 
else :
   ans = False
   print (ans)
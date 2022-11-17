# Write python program that swap two number with temp variable and without temp variable.

'''# 1_swap two number with temp variable

number1 = int (input ("Enter the number1 :- " ))
number2 = int (input ("Enter the number2 :- " ))

# Before swapping number value print
print ("Number1 = {} \t Number2 = {}".format(number1,number2))

temp = number1
number1 = number2
number2 = temp

# After swapping number value print
print ("Number1 = {} \t Number2 = {}".format(number1,number2))'''

'''# 2_swap two number without temp variable

number1 = int (input ("Enter the number1 :- " ))
number2 = int (input ("Enter the number2 :- " ))

# Before swapping number value print
print ("Number1 = {} \t Number2 = {}".format(number1,number2))

number1,number2 = number2,number1

# After swapping number value print
print ("Number1 = {} \t Number2 = {}".format(number1,number2))'''

# 3_swap two number without temp variable

number1 = int (input ("Enter the number1 :- " ))
number2 = int (input ("Enter the number2 :- " ))

# Before swapping number value print
print ("Number1 = {} \t Number2 = {}".format(number1,number2))

if number1 > number2 :
    number1 -= number2
    number2 += number1
    number1 = number2 - number1
else :
    number2 -= number1
    number1 += number2
    number2 = number1 - number2

# After swapping number value print
print ("Number1 = {} \t Number2 = {}".format(number1,number2))
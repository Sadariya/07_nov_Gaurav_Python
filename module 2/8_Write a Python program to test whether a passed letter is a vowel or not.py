# 8_Write a Python program to test whether a passed letter is a vowel or not.

# User Input
vowel = input ("Enter the alphabet to check that it is vowel or not : ")

# Using if condition check vowel or not. 
'''if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' :
    print ("It is vowel.")
else : 
    print ("It is not vowel.")'''

# Using if condition with membership operator check vowel or not.
if vowel in 'aeiou':
    print ("It is vowel.")
else :
    print ("It is not vowel.")
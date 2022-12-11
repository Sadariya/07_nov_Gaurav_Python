# 7_Write a Python program to read a file line by line store it into a variable.

import os

os.chdir('module 4')

File = open('3_Text.txt','r')

x = File.readlines()

print (x)

File.close()
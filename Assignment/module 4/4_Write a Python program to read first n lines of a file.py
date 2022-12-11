# 4_Write a Python program to read first n lines of a file.

import os

os.chdir('module 4')

File = open('1_What is File function in pythonand What is keywords to create and write file.txt','r')

lines = int (input ("Enter First n lines to show : "))

for i in range (lines):
    print(File.readline())

File.close()
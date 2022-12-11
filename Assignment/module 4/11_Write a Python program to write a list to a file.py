# 11_Write a Python program to write a list to a file.

import os

os.chdir('module 4')

File = open ('11_Text.txt','a')

list = [1,2,3,4]

File.write(f"{list}\n")

File.close()
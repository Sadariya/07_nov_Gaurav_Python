# 9_Write a Python program to count the number of lines in a text file.

import os

os.chdir('module 4')

File = open ('9_Text.txt','r') # 7 lines in this Text files

a = 0
for i in File :
    a += 1
    
print (f"Number of lines in file is : {a}")

File.close()
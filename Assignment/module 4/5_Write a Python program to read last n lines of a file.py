# 5_Write a Python program to read last n lines of a file.

import os

os.chdir('module 4')

File = open('1_What is File function in pythonand What is keywords to create and write file.txt','r')

a = True
while (a == True):
    try :
        lines = int (input ("Enter last n lines to show : "))
        a = False
    except :
        print ('Error!')

for line in (File.readlines() [-lines:]):
    
    print(line, end ='')

File.close()
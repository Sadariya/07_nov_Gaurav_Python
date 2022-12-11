# 3_Write a Python program to append text to a file and display the text.

import os 

os.chdir('module 4')

File = open ('3_Text.txt','r+')

city = input ("Enter City : ")

File.write(f"City : {city}\t\n")

# print(File.readlines())

for i in File :
    print (i)

File.close()
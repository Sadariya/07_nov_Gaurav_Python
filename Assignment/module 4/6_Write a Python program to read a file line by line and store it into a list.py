# 6_Write a Python program to read a file line by line and store it into a list

import os

os.chdir('module 4')

List = []

File = open ('2_Text.txt','r')

# print(File.readlines())

for i in File :
    print (i)
    List.append(i)

print (f"\nStore in List :- {List}")

File.close()

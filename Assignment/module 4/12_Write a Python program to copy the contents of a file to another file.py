# 12_Write a Python program to copy the contents of a file to another file.

import os

os.chdir('module 4')

x = []

# Old 3_text file data read and assign to variable for copy.
File1 =open ('2_Text.txt','r')

x = File1.readlines()

File1.close()

# New File is made and 3_text file content copy in 12_Text file.
File = open ('12_Text.txt','w')

for i in x :
    File.write(i)

File.close()
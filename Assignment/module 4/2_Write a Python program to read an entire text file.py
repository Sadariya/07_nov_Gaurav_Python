import os 

os.chdir('module 4')

File = open ('2_Text.txt','r')
a = 1

for i in File :
    print (f"{a} : {i}")
    a = a + 1
File.close()
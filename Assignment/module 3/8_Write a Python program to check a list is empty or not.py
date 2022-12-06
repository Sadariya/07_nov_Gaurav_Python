# 8_Write a Python program to check a list is empty or not.

list = ["My","apple","orange"]
count = 0

for i in list :
    count += 1

if count == 0 :
    print ("List is empty.")
else :
    if count > 0 :
        print ("List is not empty.")
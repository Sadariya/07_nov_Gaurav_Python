# 10_Write a Python program to count the frequency of words in a file.

import os

from collections import Counter

os.chdir('module 4')

File = open ('3_Text.txt','r')

x = Counter(File.read().split())

print(x)

File.close()
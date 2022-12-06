# 25_Write a Python program to reverse a tuple.

city=('Rajkot','Ahmedabad','Surat','Baroda','Navsari','Gondal')

print (f"Original tuple is : {city}")

x = list(city)

x.reverse()

print (f"Reverse tuple is : {tuple(x)}")
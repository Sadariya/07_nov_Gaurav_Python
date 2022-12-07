'''47_Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

str1 = input ("Enter Your string to count each letter and store as dictionary : ")

list1 = list()
list2 = list()
count = 0

for i in str1 :
    for j in str1 :
            if i in j :
                count += 1
    if i != " ":
        list1.append(i)
        list2.append(count)
    count = 0

print (f"Original string is : {str1}")
print (f"Output is : {dict(zip(list1,list2))}")
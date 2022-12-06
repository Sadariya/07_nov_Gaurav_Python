''' 
6_Write a Python program to count the number of strings 
where the string length is 2 or more and the first and
last character are same from a given list of strings.
'''
# Static list :
list = ["rajr","tant","Ujash","kailashk","ab"]

# User-difine list :
'''
list = []
n = int(input("Enter the list of items :-"))
for i in range (n):
    list_item = input("Enter the item of list :- ")
    list.append(list_item)

'''
# count variable to assign to integer function :-
count = int()

# Loop is used to check that number is less than 2 then check that the string first and last character is same or not

for i in list :
    L = len (i)
    if L >= 2 :
        if i[0] == i[-1] :
            count += 1
            print(f"{count} : {i}")

# Print the output number of string :- 
print (f"Number of string is : {count}")
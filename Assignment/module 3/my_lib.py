def factorial () :
    number = int (input ("Enter the number to find factorial of numbers : "))
    res = 1
    for i in range (number):
        res = res * (i+1)
    print (f"Factorial of {number} is : {res}")

def user_list () :
    list1 = []
    n = int(input("Enter the list of items :-"))
    for i in range (n):
        list_item = input("Enter the item of list")
        list1.append(list_item)
    return list1


# 5_How will you compare two lists?

# list1 = []
# n = int (input ("Enter the number to run loop : "))
# for i in range (n) :
#     num = int (input ("Enter the number : "))
#     list1.append(num)
# print (list1)

# list2 = []
# n = int (input ("Enter the number to run loop : "))
# for i in range (n) :
#     num = int (input ("Enter the number : "))
#     list1.append(num)
# print (list1)

from my_lib import user_list

list1 = user_list ()
list2 = user_list ()


# list1 = [11,12,13,14,15]
# list2 = [15,12,11,12,14]

list1.sort()
list2.sort()

if list1 == list2 :
    print ("These are equal list.")
else :
    print ("These are not equal list.")
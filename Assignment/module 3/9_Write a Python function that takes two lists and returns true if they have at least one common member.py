# 9_Write a Python function that takes two lists and returns true if they have at least one common member.

from my_lib import user_list

# user-define list using module :- 
list1 = user_list()
list2 = user_list()

# static list
'''
list1 = ["My","Gaurav","Jatin","Mi"]
list2 = ["Mine","Jatin","Jay","Gaurav"]
'''

def common_member (list1,list2) :
    x = False

    for i in list1 :
        for j in list2 :
            if i == j :
                x = True

    return x

print (common_member(list1,list2))
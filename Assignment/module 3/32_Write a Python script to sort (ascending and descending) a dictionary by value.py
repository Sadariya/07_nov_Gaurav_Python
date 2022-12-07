# 32_Write a Python script to sort (ascending and descending) a dictionary by value.

# User-define function :-
def sort_dictionary (dic , revrse=True) :
    return dict(sorted(dic.items(), key = lambda x : x[1], reverse=revrse))

# static dictionary :- 
dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}

# print the output

print (f"Ascending order is : {sort_dictionary(dic,False)}")

print (f"Descending order is : {sort_dictionary(dic)}")
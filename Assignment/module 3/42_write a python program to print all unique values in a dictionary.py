# 42_write a python program to print all unique values in a dictionary

# user input dictionary :- 
from my_lib import user_dict 

x = user_dict ()

print (f"dictionary is : {x}")

# static dictionary
# x = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}

y = set(x)
print (f"Unique values of dictionary : {y}")
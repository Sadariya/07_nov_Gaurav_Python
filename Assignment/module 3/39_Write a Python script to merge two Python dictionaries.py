# 39_Write a Python script to merge two Python dictionaries

dict1 = {1:'Name',2:'Age',3:'sub'}
dict2 = {4:16,5:25,6:24,7:49}

# 1) Using | operator :-
print (dict1|dict2)

# 2) Using ** operator :-
print (f"Using the ** operator :-",{**dict1,**dict2})

# 3) Using copy and update function :-
dict3 = dict2.copy()
dict3.update(dict1)

print (f"Using the copy and update function :- {dict3}")
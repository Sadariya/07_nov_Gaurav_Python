
'''
What is used to check whether an object o is an instance of class A?
--> using is instance() , we can check that class A object o or not
    If o is not object of class A it gets false otherwise it gives 
    true.
'''

class A :
    pass

o = A ()

print (isinstance(o,A))
print(isinstance(o, (list, tuple)))
print(isinstance(o, (list, tuple, A)))
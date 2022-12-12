# 22_How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
'''
How to Define a class in Python ?
--> Using Class keyword we can define class.

What is self ?
--> If method is declared in class. Argument 
    must be declared in the function.

self represents the instance of the class.
By using the “self” we can access the attributes and methods of the class in python.
It binds the attributes with the given arguments.
The reason you need to use self is because Python does not use the @ syntax to refer to instance attributes.
'''
# Create a class using class keywords :-
class Python :

    Name = input ("Enter Your Name :- ")

    school = input ("Enter Your school name :- ")
    # Using Self we can access data member of class in member function. :- 
    def printdata (self):
        print (f"Your School name is {self.school}")

# Create an object
pt = Python ()
# Call the class using object
print(f"Your name is :{pt.Name}")
pt.printdata()
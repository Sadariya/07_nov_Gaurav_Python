'''
23_Write a Python class named Rectangle constructed by a length and width and
a method which will compute the area of a rectangle
''' 

class Rectangle :
    # Length and Width :-
    Length = float (input ("Enter the Length of Rectangle :- "))
    Width = float (input ("Enter the Width of Rectangle :- "))
    # Method of area of rectangle :-
    def Area_Rectangle (self) :
        Area = self.Length * self.Width
        print ("\nArea of Rectangle is :- ",Area)

Re = Rectangle ()
Re.Area_Rectangle()
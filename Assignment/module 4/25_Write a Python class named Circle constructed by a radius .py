''' 
25_Write a Python class named Circle constructed by a radius 
and two methods which will compute the area and the perimeter of a circle
'''
import math

class Circle :
    
    Radious = float (input ("Enter the Radious of circle :- "))

    def Area_Circle (self):

        Area = math.pi * pow(self.Radious,2)
        print ("Area of Circle is : ",Area)
    
    def perimeter_Circle (self) :

        Perimeter = 2 * math.pi * self.Radious
        print ("Perimeter of Circle is : ",Perimeter)


Cr = Circle ()

Cr.Area_Circle()
Cr.perimeter_Circle()
# 62_Write a Python program to calculate surface volume and area of a cylinder

# A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r².

import math

def cylinder_volume (radious,height) :
    cylinder_vol = math.pi*(radious*radious)* height
    return cylinder_vol

def cylinder_area (radious,height) :
    cylinder_ar = (2*math.pi*radious*height) + (2*math.pi*(radious*radious))
    return cylinder_ar

x = cylinder_volume (10,5)
y = cylinder_area(12,25)

print (f"Volume of cylinder is : {x}")
print (f"Area of cylinder is : {y}")
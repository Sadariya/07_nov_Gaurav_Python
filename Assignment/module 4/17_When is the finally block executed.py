'''
17_ When is the finally block executed

--> Fianlly block executed every time when run the 
    try/except block.

--> like,Example is given below.
'''

A = True

while (A== True) :
    try : 
        number = int(input ("Enter the number :- "))
        A = False
    except:
        print (f"Error!")
    else :
        print ("Yes Finally you did it")
    finally :
        print ("Good to See you here.")

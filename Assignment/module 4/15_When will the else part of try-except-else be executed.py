'''
15_When will the else part of try-except-else be executed?

--> try-except-else in else part will be executed when try block
    is true and it is excecuted , else part will be excecuted.

'''


try :
    number = int (input("Enter the number : "))
except :
    print ('error!')
else :
    print ('This is Else part.')
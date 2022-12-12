'''
26_Explain Inheritance in Python with an example?
What is init?
Or What Is A Constructor In Python?
'''
# Explain Inheritance in Python with an example?
# --> Inheritance means which is use the property of other class.

class Python :

    Python_Student = int(input ("Enter Python's Students :"))
    Java_Student = int (input("Enter Java's Student :"))


class Inheritance (Python) :
    
    def readdata (self):
        print ("Python Student is :",self.Python_Student)
        print ("Java Student is :",self.Java_Student)

In = Inheritance ()

In.readdata()
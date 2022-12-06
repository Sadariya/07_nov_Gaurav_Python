# 14_Write a Python program to find the second smallest number in a list.

# List = [6,5,1,2,4,3]

# User-define list :- 
List = []

Number = int(input("Enter the number :- "))

for i in range (Number) :
    number = int (input ("Enter the number to make a list :- "))
    List.append (number)

# Print Original list :- 
print (f"Original list : {List}")
# Sort the list :- 
List.sort ()
# print the index of second numbers :-
print(List[1])
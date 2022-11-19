'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
   If the given string already ends with 'ing' then add 'ly' instead if the string length of the 
   given string is less than 3, leave it unchanged.'''
for i in range (3):
   spelling = input ("Enter the spelling : ")
   add = "ing"

   if spelling [-3:] == 'ing' :
      x = spelling.replace ('ing','ly')
      print (x)

   elif len(spelling) >= 3:
      spelling = spelling + add
      print (spelling)

   else :
      print (spelling)
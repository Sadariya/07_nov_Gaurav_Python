'''18_Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
   If the given string already ends with 'ing' then add 'ly' instead if the string length of the 
   given string is less than 3, leave it unchanged.'''

# Loop is used to perform 3 times program
for i in range (3):
   # User Input the spelling
   spelling = input ("Enter the spelling : ")
   add = "ing"
   # If ing found at the end of spelling then change ing to lys
   if spelling [-3:] == 'ing' :
      x = spelling.replace ('ing','ly')
      print (x)
   # If spelling do not have ing at the end of spelling then add ing 
   elif len(spelling) >= 3:
      spelling = spelling + add
      print (spelling)
   # If spelling length is less than 3 then print same as word
   else :
      print (spelling)
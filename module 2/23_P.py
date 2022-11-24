# 23_Write a Python function to insert a string in the middle of a string

# User Input
str = input ("Enter the string : ")

# Length of string is count
Length_str = len (str)

# mid length is count
mid_Len = Length_str // 2

# User Input Middle string 
Mid_str = input ("Enter Your middle string : ")

# Print the final output
print (str[:mid_Len] + Mid_str + str[mid_Len :])
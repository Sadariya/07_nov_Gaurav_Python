''' 
19_Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace
the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''
# Static Input
string = "he is not so poor in village."

# x assign to replace not to space
x = string.replace("not","\b")

# Again x assign to poor to good
x = x.replace("poor","good")

# print final output
print(x)

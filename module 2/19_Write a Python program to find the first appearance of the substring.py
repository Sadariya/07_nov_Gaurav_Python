''' 
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace
the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''
string = "he is not so poor in village."

x = string.replace("not","\b")
x = x.replace("poor","good")

print(x)

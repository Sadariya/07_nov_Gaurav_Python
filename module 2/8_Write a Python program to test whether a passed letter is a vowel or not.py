vowel = input ("Enter the alphabet to check that it is vowel or not : ")

'''if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' :
    print ("It is vowel.")
else : 
    print ("It is not vowel.")'''

if vowel in 'aeiou':
    print ("It is vowel alphabet.")
else :
    print ("It is not vowel alphabet.")
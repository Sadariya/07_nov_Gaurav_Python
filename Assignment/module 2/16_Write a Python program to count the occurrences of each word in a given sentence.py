# 16_Write a Python program to count the occurrences of each word in a given sentence

# Static Input
string = "My name is Gaurav and I am a student of tops career at Rajkot."

# assign count variable to 0 
count = 0

# count the each word using loop but space not count
for i in string:
    if i != " ":
        count = count + 1

print ("String words count without space is ",count)
print ("String words count without space is ",len(string))
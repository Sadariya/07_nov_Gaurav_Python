''' 54_How can you pick a random item from a range?

--> There are two method to pick a random item 
    from a range.
    1) randrange
    2) randint'''

import random

x = random.randrange(1,100)
# Using the randrange function of random module
print (f"random items from 1 to 100 is :- {x}")
# Using the randint function of random module
y = random.randint(1,100)

print (f"random items from 1 to 100 is :- {y}")
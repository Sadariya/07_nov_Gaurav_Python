# 53_How can you pick a random item from a list or tuple?

import random

for i in range (3):
        
    list1 = [1,2,3,4,5]
    tuple1 = (1,2,3,4,5)

    l=random.choice(list1)
    t = random.choice(tuple1)

    print (f"random items from list is : {l} \nrandom itmes form tuple is {t}")
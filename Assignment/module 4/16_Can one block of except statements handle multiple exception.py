# 16_Can one block of except statements handle multiple exception?

# Single except statement :- 
try:
    name = 'Bob'
    name += 5
except (NameError, TypeError) as error:
    print(error)

# Multiple except statement :- 
try:
    name = 'Bob'
    name =+ 5
except NameError as ne:
    # Code to handle NameError
    print(ne)
except TypeError as te:
    # Code to handle TypeError
    print(te)

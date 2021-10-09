# Game to determine which function has access to whih variables
a = 59

def confusion():
    a = 5
    return a

print(a)
print(confusion())

'''
    Scoping Rules

    1. Start with Local scope
    2. look inside higher scope, a parent local scope
    3. Look into Global scope for any non-found variables
    4. Built in Python functions
'''
# Argument and Key Word  Argument in Python
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=3,num2=18))

# Follow the Rule

'''
    1. params
    2. *args
    3. default parameters
    4. **kwargs
'''
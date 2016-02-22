# Learning and playing with decorators
def banstring(func):
    def wrapper(arg):
        if type(arg) == int:
            return func(arg)
        else:
            return 'Must be int.'
    return wrapper

@banstring
def addone(num):
    return num + 1


# applying function decorator to class methods:

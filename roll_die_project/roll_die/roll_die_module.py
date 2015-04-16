import random
def roll_die(side_num):
    '''
    The input argument represents the sides of an abstract die which
    could be normal six-sided die otherwise with more or less sides in
    spite of physical feasibility.
    '''
    return random.randint(1, side_num)

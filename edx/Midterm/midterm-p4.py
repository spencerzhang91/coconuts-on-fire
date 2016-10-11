def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    while base ** exp < num:
        exp += 1
    prev_exp = exp - 1
    if abs(base ** prev_exp - num) <= abs(base ** exp - num):
        return prev_exp
    else:
        return exp


print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))

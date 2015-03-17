def check(password):
    if len(password) >= 10:
        upper_list = [x for x in password if x.isupper()]
        lower_list = [x for x in password if x.islower()]
        digit_list = [x for x in password if x.isdigit()]
        if (len(upper_list) * len(lower_list) * len(digit_list)) != 0:
            return True
        else:
            return False
    else:
        return False

# test code:

p1 = 'aA12agadfaa2222'
p2 = 'a11sdgadgaaaae1'
p3 = 'Aaaafadfafaaa'
p4 = 'A111AADGAHTSADA111'
p5 = 'Aa1Aa1Aa1Aa1'
p6 = '111'

t1 = print(check(p1))
t2 = print(check(p2))
t3 = print(check(p3))
t4 = print(check(p4))
t5 = print(check(p5))
t6 = print(check(p6))

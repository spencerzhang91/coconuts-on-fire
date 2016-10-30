def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if int(us_num) <= 10:
        return trans[us_num]
    elif 11 <= int(us_num) <= 19:
        return "shi " + trans[us_num[1]]
    elif int(us_num) % 10 == 0 and us_num != "10":
        return trans[us_num[0]] + " shi"
    else:
        return trans[us_num[0]] + " shi " + trans[us_num[1]]


trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

a = convert_to_mandarin("0")
b = convert_to_mandarin("9")

c = convert_to_mandarin("13")
d = convert_to_mandarin("39")
e = convert_to_mandarin("40")

print(a, b, c, d, e, sep='\n')

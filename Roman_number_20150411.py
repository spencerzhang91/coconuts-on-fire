def convertor(num):
    '''
    A function that convert integer less than 4000 to Roman number.
    '''
    if type(num) == int and num < 4000:
        # Dictionary of convertion
        Hundreds = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC',
                    7:'DCC', 8:'DCCC', 9:'CM', 0:''}
        Tens = {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX',
                8:'LXXX', 9:'XC', 0:''}
        Ones = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII',
                8:'VIII', 9:'IX', 0:''}
        
        
        tho = num // 1000
        hun = (num - tho*1000) // 100
        ten = (num - tho*1000 - hun*100) // 10
        one = num - tho*1000 - hun*100 - ten*10
        
        res = 'M'*tho + Hundreds[hun] + Tens[ten] + Ones[one]
        return res

    else:
        return 'The number should be integer and less than 4000.'
        

# 别人家的代码来了：
'''
elements = { 1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 
             100 : 'C', 90 : 'XC', 50 : 'L', 40: 'XL', 
             10 : 'X', 9 : 'IX', 5 : 'V', 4: 'IV', 1 : 'I' }
             
def checkio(data):
    roman = ''
    
    for n in sorted(elements.keys(), reverse=True):
        while data >= n:
            roman += elements[n]
            data -= n
​
    return roman
'''
# 真的好简洁有木有。。。




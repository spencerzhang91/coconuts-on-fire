def speaker(number):
    num = number
    d = len(str(num))

    def ten_one(n):
        if d == 1:
            res = FIRST_TEN[n-1]
        elif d == 2:
            if n // 10 == 1:
                res = SECOND_TEN[n-10]
            else:
                if n%10 != 0:
                    res = OTHER_TENS[n//10-2] + ' ' + FIRST_TEN[n%10-1]
                else:
                    res = OTHER_TENS[n//10-2]
        else:
            res = 'wtf'

        return res

    if d < 3:
        outcome = ten_one(num)
        return outcome
    else:
        h = FIRST_TEN[num//100-1]
        d = len(str(num%100))
        if num%100 != 0:
            e = ' ' + ten_one(num%100)
        else:
            e = ''
        return (h + ' ' + HUNDRED + e)



FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"




for i in range(1000):
    print(i, speaker(i))
    
'''
def checkio(number):
​
    n = number // 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []
​
    n = (number // 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []
​
    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []
​
    return ' '.join(t)

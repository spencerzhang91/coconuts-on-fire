def main():
    print('Please enter x as base and exp as exponent.')
    try:
        while 1:
            x = float(input('x = '))
            exp = int(input('exp = '))
            print(x ** exp)
    except:
        print('end')
    
main()
        

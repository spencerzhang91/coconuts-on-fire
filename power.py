def main():
    print('Please enter x as base and exp as exponent.')
    try:
        while 1:
            x = float(input('x = '))
            exp = int(input('exp = '))
            print("%.3f to the power %d is %.5f\n" % (x,exp,x ** exp))
            print("Please enter next pair or q to quit.")
    except:print('Hope you enjoyed the power trip...')    
main()
        

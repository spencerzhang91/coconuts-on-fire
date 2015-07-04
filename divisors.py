num = input("Please enter an integer for analysis; Enter q to quit.\n")   
while num.isnumeric():
    num = int(num)
    isPrime = True
    for div in range(2, int(num ** 0.5)+1):     
        if num % div == 0:
            if div != num ** 0.5:
                print("%d is divisible by %d and %d.\n" %\
                      (num, div, num/div))   
            else:
                print("%d is divisible by %d.\n" % (num, div))
            isPrime = False      
    if isPrime:
        print("%d is prime." % num) 
    num = input("Please enter another integer for analysis; Enter q to quit.\n")
print('Bye.\n')
            

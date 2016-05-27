import time
import random

def timer(calls=1):
    def decorator(func):
        def wrapper(*args):
            t1 = time.time()
            for i in range(calls):
                func(*args)
            t2 = time.time()
            print(t2 - t1)
        return wrapper
    return decorator

# demos:
if __name__ == "__main__":
    @timer(calls=100000)
    def addition(a):
        for i in range(a):
            for j in range(a):
                x = 1

    @timer(calls=100000)
    def multiply(b):
        for i in range(b):
            y = 1

    addition(100)
    multiply(100)

"""
result:
=============== RESTART: C:/Users/Spencer/Desktop/timerdeco.py ===============
17.63799524307251
0.20052003860473633
"""

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested
        
f = tester(0)
f('spam')
f('what')
g = tester(20)
g('gogogo')
g('why?')
f('omg')
    

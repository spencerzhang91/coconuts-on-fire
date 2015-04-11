# File timer.py
'''
Homegrown timing tools for function calls.
Does total time, best-of-time, and best-of-total time
'''
import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, _resp=1000, **kargs):
    '''
    Total time to run func() reps times.
    Return (total time, last result)
    '''
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return(elapsed, ret)

def bestof(func, *pargs, _resp=5, **kargs):
    '''
    Quickest func() among reps runs.
    Return (best time, last result)
    '''
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _resp1=1000, **kargs):
    '''
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    '''
    return min(total(func, *pargs, **kargs) for i in range(_reps1))

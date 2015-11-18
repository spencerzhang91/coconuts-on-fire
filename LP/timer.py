# File timer.py
'''
Homegrown timing tools for function calls.
Does total time, best-of-time, and best-of-total time
'''
import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

<<<<<<< HEAD
def total(func, *pargs, _resp=1000, **kargs):
=======
def total(reps, func, *pargs, **kargs):
>>>>>>> 648552c5a5e7c2aac5c96407cae3e33a87b73e99
    '''
    Total time to run func() reps times.
    Return (total time, last result)
    '''
<<<<<<< HEAD
    start = timer()
    for i in range(_reps):
=======
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
>>>>>>> 648552c5a5e7c2aac5c96407cae3e33a87b73e99
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return(elapsed, ret)

<<<<<<< HEAD
def bestof(func, *pargs, _resp=5, **kargs):
=======
def bestof(reps, func, *pargs, **kargs):
>>>>>>> 648552c5a5e7c2aac5c96407cae3e33a87b73e99
    '''
    Quickest func() among reps runs.
    Return (best time, last result)
    '''
    best = 2 ** 32
<<<<<<< HEAD
    for i in range(_reps):
=======
    for i in range(reps):
>>>>>>> 648552c5a5e7c2aac5c96407cae3e33a87b73e99
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)

<<<<<<< HEAD
def bestoftotal(func, *pargs, _resp1=1000, **kargs):
=======
def bestoftotal(reps1, reps2, func, *pargs, **kargs):
>>>>>>> 648552c5a5e7c2aac5c96407cae3e33a87b73e99
    '''
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    '''
<<<<<<< HEAD
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
=======
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
>>>>>>> 648552c5a5e7c2aac5c96407cae3e33a87b73e99

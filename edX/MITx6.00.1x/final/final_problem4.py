def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest = []
    for i in range(len(L) - 1):
        if L[i] <= L[i+1]:
            increasing = True
            increase = [L[i]]
        else:
            increasing = False
            decrease = [L[i]]
        for j in range(i+1, len(L)):
            if L[j] >= L[j-1] and increasing:
                increase.append(L[j])
            elif L[j] <= L[j-1] and not increasing:
                decrease.append(L[j])
            else:
                if increasing and len(increase) > len(longest):
                    longest = increase[:]
                    increase = []
                elif not increasing and len(decrease) > len(longest):
                    longest = decrease[:]
                    decrease = []
                i = j - 1
                break
    # print(longest)
    return sum(longest)

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
result = longest_run(L)
print(result)
            

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def func(num):
        poly = 0
        for i in range(len(L)):
            poly += L[i] * num ** (len(L) - 1 - i)
        return poly
    return func


result = general_poly([1,2,3,4])(10)
print(result)
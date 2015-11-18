class Truth:
    '''
    The __bool__ method is prefered over __len__ in python.
    '''
    def __bool__(self):
        return True
    def __len__(self):
        return 0

if __name__ == "__main__":
    X = Truth()
    if X: print("Yes!");
# Defination of python list based Deque (Double ended queue) ADT
# A exception class define for handling empty errors

class Empty(Exception):
    '''
    Error attemping to access an element from an empty container.
    '''
    pass

class Deque:
    '''
    A special case of queue which can add and delete elements from both
    ends. Using a python list as underlying storage.'''
    DEFAULT_CAPACITY = 10
    def __init__(self):
        '''Create empty deque.'''
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def __len__(self):
        '''Return the number of elements in the deque.'''
        return self._size

    def is_empty(self):
        '''Return True if the deque is empyt.'''
        return self._size == 0

    def first(self):
        '''Return (but do not remove) the element at the front of the queue.
    Raise Empty exception if the deque is empty.'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        '''Return (but do not remove) the element at the end of the queue.
    Raise Empty exception if the deque is empty.'''
        if self.is_empty():
            raise Empty('Deque is empty')
        # self._back = (self._front + self._size - 1) % len(self._data)
        return self._data[self._back]

    def add_first(self, e):
        '''Add element e to the front of deque.'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))                   # extend capacity
        self._front = (self._front - 1) % len(self._data)       # cyclic shift
        self._data[self._front] = e        
        self._size += 1
 
    def add_last(self, e):
        '''Add element e to the back of deque.'''
        if self._size == len(self._data):
            self._resize(2* len(self._data))
        self._back = (self._back + self._size) % len(self._data)
        self._data[self._back] = e
        self._size += 1

    def delete_first(self):
        '''Remove and return the first element of the deque,
    Raise Empty exception if the deque is empty.'''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)       # i.e.,DEFAULT_CAPACITY
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)                    # shrink list by 1/2 after
        return answer

    def delete_last(self):
        '''Remove and return the last element of the deque,
    Raise Empty exception if the deque is empty.'''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)       # i.e.,DEFAULT_CAPACITY
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)                    # shrink list by 1/2 after
        return answer

    def _resize(self, cap):
        '''Resize to a new list of capacity >= len(self)'''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):                             # self._size here is old size
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0                                         # self._front realigned


if __name__ == '__main__':
    def explore(deque):
        print("The deque under test --> ID: %d" % id(deque))
        print("element number --> %d" % len(deque))
        print("first element --> %d" % deque.first())
        print("last element --> %d" % deque.last())
        print("underlying data --> %s" % str(deque._data))
        print("current front index --> %d" % d._front)
        print("current back index --> %d" % d._back)
        print()

    d = Deque()
    d.add_first(1)
    d.add_last(2)
    explore(d)
    d.add_first(11)
    d.add_last(22)
    explore(d)
    d.add_first(111)
    d.add_last(222)
    explore(d)
    d.add_first(1111)
    d.add_last(2222)
    explore(d)
    



        

    

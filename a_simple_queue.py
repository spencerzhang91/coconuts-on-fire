class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the length of the queue.
        """
        return len(self._items)

    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """
        return self._items.append(item)

    def dequeue(self, item):
        """
        Remove item from the queueu.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items in the queue.
        """
        self._items = []

queue = Queue()
print(len(queue))
queue.enqueue(33)
queue.enqueue(44)
for item in queue:
    print(item)

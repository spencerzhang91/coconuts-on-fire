class Queue:
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.qcount = 0

    def __len__(self):
        return self.qcount

    def isEmpty(self):
        return self.qcount == 0

    def enqueue(self, item):
        node = self.QueueNode(item)
        if self.isEmpty():
            self.qhead = node
        else:
            self.qtail.next = node
        self.qtail = node
        self.qcount += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from empty queue."
        node = self.qhead
        if self.qhead is self.qtail:
            self.qtail = None
        self.qhead = self.qhead.next
        self.qcount -= 1
        return node.item
    
    class QueueNode:
        def __init__(self, item):
            self.item = item
            self.next = None


if __name__ == "__main__":
    testq = Queue()
    testq.enqueue(3)
    testq.enqueue(4)
    a = testq.dequeue()
    b = testq.dequeue()
    print(a, b)

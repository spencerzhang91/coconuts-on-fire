# list node definetion:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "[%s --> %s]" % (self.val, self.next)

    def __str__(self):
        return str(self.val)

    def traverse(self):
        rec = []
        while self:
            rec.append(self.val)
            self = self.next
        print(rec)

# Test code:
if __name__ == '__main__':
    
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(2)
    n3 = ListNode(9)
   

    n0.next = n1; n1.next = n2; n2.next = n3
    h = n0
    h.traverse()
    test = Solution()
    res = test.deleteDuplicates(h)
    try:
        res.traverse()
    except AttributeError:
        print(res)

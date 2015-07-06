# a linked list(here the singly linked list) must have a head reference(pointer), otherwise it would
# be impossible to locate the head or any other node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

def traverse(head):
    curNode = head
    while curNode != None:
        print(curNode)
        curNode = curNode.next

def unorderedSearch(head, target):
    curNode = head
    while curNode != None and curNode.val != target:
        curNode = curNode.next
    return curNode is not None
    


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = None

a.next = b
b.next = c
c.next = d
d.next = e

b = c = d = e = None
#print(a)

traverse(a)
print(unorderedSearch(a, 3))

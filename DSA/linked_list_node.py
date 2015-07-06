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
    

head = ListNode('A')
n1 = ListNode('B')
n2 = ListNode('C')
n3 = ListNode('D')
# connect the nodes
head.next = n1
n1.next = n2
n2.next = n3
# traverse(head)

def reverse(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
        print('->', prev, curr, head)
    return prev

reverse(head)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
mid = ListNode(34)
tail = ListNode(4)
head.next = mid
mid.next = tail
mid = tail = None
print(head.val)
print(head.next.val)
print(head.next.next.val)


# a linked list(here the singly linked list) must have a head reference(pointer), otherwise it would
# be impossible to locate the head or any other node.

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

def removeNode(head, target):
    prev = None
    curr = head
    while curr and curr.val != target:
        prev = curr
        curr = curr.next
    if curr:
        if curr is head:
            head = curr.next # what about "head = head.next"?
        else:
            prev.next = curr.next
            curr.next = None # disconnect the removed node with it's next node
            
def reverse(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def reverse_rec(head):
    if not head:
        return None
    if not head.next:
        return head
    curr = head.next
    new_head = reverse_rec(curr)
    head.next = None
    curr.next = head
    return new_head

if __name__ == '__main__':
    n0 = ListNode('A')
    n1 = ListNode('B')
    #n2 = ListNode('C')
    #n3 = ListNode('D')
    n0.next = n1
    print(reverse(n0))
    print(reverse_rec(n0))

    
    
    
    

# A function that creates linked list from a python list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return str(self.val)

    
def CreateLinkedList(infolist):
    '''
    The infolist is a python list contains structure information, this
    function returns the head node of the constructed linked list.
    '''
    curr = head = ListNode(None)
    for item in infolist:
        node = ListNode(item)
        curr.next = node
        curr = curr.next
    head = head.next
    return head

if __name__ == '__main__':
    newlist = CreateLinkedList([1,2,3,4,5,6])
        
    
    

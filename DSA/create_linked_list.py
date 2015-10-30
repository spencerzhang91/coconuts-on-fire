# two useful helper function of linked list

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


def CreateList(array):
	head = Node(0)
	curr = head
	for item in array:
		node = Node(item)
		curr.next = node
		curr = curr.next
	return head

def DisplayList(head):
	while head:
		print(str(head.val) + "->", end='');
		head = head.next

if __name__ == '__main__':
	l = CreateList([1,2,3,4,5])
	DisplayList(l)



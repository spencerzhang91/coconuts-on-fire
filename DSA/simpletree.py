# create a simple tree data structure with python
# First of all: a class implemented to present tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def addnode(self, new):
        if self.root == None:
            self.root = new
            self.size += 1
        else:
            self.helper(self.root, new)

    def helper(self, innode, new):
        if innode == None:
            innode = new
            self.size += 1
            
        elif new.val < innode.val:
            if innode.left == None:
                innode.left = new
                self.size += 1
            else:
                self.helper(innode.left, new)
                
        elif new.val > innode.val:
            if innode.right == None:
                innode.right = new
                self.size += 1
            else:
                self.helper(innode.right, new)
        else:
            print("can't have duplicate node!")


def Inorder(root):
    if root != None:
        Inorder(root.left)
        print(root.val, end=" ")
        Inorder(root.right)


elderwood = Tree()

n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(22)
n4 = TreeNode(1)
n5 = TreeNode(0)

n6 = TreeNode(-7)
n7 = TreeNode(8)

n8 = TreeNode(100)
n9 = TreeNode(-50)

elderwood.addnode(n1)
elderwood.addnode(n2)
elderwood.addnode(n3)
elderwood.addnode(n4)
elderwood.addnode(n5)
elderwood.addnode(n6)
elderwood.addnode(n7)
elderwood.addnode(n8)
elderwood.addnode(n9)

Inorder(elderwood.root)
print("\nTotal tree nodes: %d" % elderwood.size)


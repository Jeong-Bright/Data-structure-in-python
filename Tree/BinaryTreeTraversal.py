from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Binarytree():
    def __init__(self):
        self.root = None
    
    def preorder(self, n):
        if n != None:
            print(n.data,end = " ")
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)
    def inorder(self, n):
        if n!= None:
            if n.left:
                self.inorder(n.left)
            print(n.data, end=" ")
            if n.right:
                self.inorder(n.right)
    def postorder(self, n):
        if n!=None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.data, end=" ")
    def levelorder(self, root):
        q=[]
        q.append(root)
        while q:
            a=q.pop(0)
            print(a.item, end=" ")
            if a.left != None:
                q.append(a.left)
            if a.right != None:
                q.append(a.right)
    def height(self, root):
        if root == None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

BT = Binarytree()
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
N8 = Node(8)

BT.root = N1
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8


print("preorder : ", end="")
BT.preorder(BT.root)
print("inorder : ", end = " ")
BT.inorder(BT.root)
print("postorder : ", end = " ")
BT.postorder(BT.root)
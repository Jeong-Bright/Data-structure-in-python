from MyList import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
         
class LinkedList:
    
    def __init__(self, head=None):
        self.nodeCount = 0
        self.head = None
    def len(self):
        return self.nodeCount
    
    def getitem(self, j):
    
        if self.nodeCount > j:
            for i in range(j):
                cur = cur.next_node
            return cur.data
        raise ValueError('Value not in list !')
    def setitem(self, val, j):
        if self.nodeCount > j:
            cur = self.head
            for i in range(j):
                cur = cur.next_node
            cur.data = val
            return
        raise ValueError('index is out of bounds !')
    def insertitem(self, item, j=0):
        N_node = Node(item)
        if j == 0:
            N_node.set_next(self.head)
            self.head = N_node
            self.nodeCount += 1
            
        elif j>0 and j < self.length -1:
            cur = self.head
            for i in range(j-1):
                cur = cur.next_node
            temp = cur.next_node
            cur.next_node = N_node
            N_node.set_next(temp)
            self.length += 1
    
    def removeitem(self, j=0):
        if j == 0:
            self.head = self.head.next_node
        elif j < self.length -1:
            cur=self.head
            for i in range(j-1):
                cur = cur.next_node
            cur.next_node = cur.next_node.next_node
        elif j == self.length -1:
            cur = self.head
            for i in range(j-1):
                cur = cur.next_node
            cur.next_node = None
            
    def printmylist(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end = " ")
            ptr = ptr.next_node
        print()
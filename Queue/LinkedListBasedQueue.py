from MyQueue import *

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedListBasedQueue:
    
    def __init__(self, head, tail):
        self.head =None
        self.tail = None
        self.length = 0
        
    def len(self):
        return self.length
    
    def first(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.head.data
        
    def is_empty(self):
        if self.length == 0:
            return True
        else: return False
        
    def enqueue(self, item):
        N_node = Node(item)
        if self.is_empty():
            self.head = N_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next_node = N_node
            self.tail = N_node
            self.length +=1
    
    def dequeue(self, j=0):
        if self.is_empty():
            print("Queue is empty")

        else:
            self.head.next_node = self.head
            self.length -= 1
        
    def printmylist(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end = ' ')
            ptr = ptr.next_node
        print(" ")
        

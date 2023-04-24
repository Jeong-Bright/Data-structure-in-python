class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class SLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.length = 0
        
    def listlength(self):
        return self.length
    
    def is_empty(self):
        if self.length != 0:
            return False
        else:
            return True
        
    def selectNode(self, idx):
        if idx >= self.length:
            print("index error")
        if idx == 0:
            return self.head
        else:
            t = self.head
            for i in range(idx-1):
                t = t.next
            return t
                
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.length += 1
        
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.length += 1
        else:
            t = self.head
            while t.next != None:
                t = t.next
            New = Node(value)
            t.next = New
            self.length += 1
            
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.length += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.length += 1
        else:
            t = self.head
            for i in range(idx):
                t = t.next
            NewNode = Node(value)
            nxt = t.next
            t.next = NewNode
            NewNode.next = nxt
            self.length += 1
                    
    def delete(self, idx):
        if self.is_empty():
            print("list is empty")
        elif idx >= self.length:
            print("index over")
        elif idx == 0:
            t = self.head
            self.head = t.next
            del(t)
            self.length -= 1
        else:
            t = self.selectNode(idx)
            delt = t.next
            t.next = t.next.next
            del(delt)
            self.length -= 1
            
            
        
    def printlist(self):
        t = self.head
        while t:
            if t.next != None:
                print(t.data, '->', end = ' ')
                t = t.next
            else:
                print(t.data)
                t = t.next


a = SLinkedList()

a.appendleft(5)
a.append(2)
a.delete(1)

a.printlist()
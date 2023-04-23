class Node(object):
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
        
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
        
    def len(self):
        return self.size
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
        
    def selectNode(self, idx):
        if idx > self.size:
            print("Overflow")
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size/2:
            t = self.head
            for i in range(idx):
                t = t.next
            return t
        else:
            t = self.tail
            for i in range(self.size - idx):
                t = t.prev
                return t

    def appendleft(self, value):
        if self.is_empty():
             self.head = Node(value)
             self.tail = Node(None, self.head)
             self.head.next = self.tail
        else:
             tmp = self.head
             self.head = Node(value, None, self.head)
             tmp.prev = self.head
        self.size += 1
    
    def append(self, value):
         if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
         else:
            tmp = self.tail.prev
            NewNode = Node(value, tmp, self.tail)
            tmp.next = NewNode
            self.tail.prev = NewNode
         self.size += 1
        
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
            
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.head:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
            self.size += 1
            
    def delete(self, idx):
        if self.is_empty():
             print("empty")
             return
        else:
             tmp = self.selectNode(idx)
             if tmp == None:
                  return
             elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
             elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
             else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
             del(tmp)
             self.size -= 1
                
    def printlist(self):
        tar = self.head
        while tar != self.tail:
            if tar.next != self.tail:
                print(tar.data, '<=>', end = ' ')
            else:
                print(tar.data)
            tar = tar.next
        
        
mylist = DoublyLinkedList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.len())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()
            
                
                
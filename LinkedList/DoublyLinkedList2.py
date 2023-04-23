from MyList import MyList
class Node(object):
    def __init__(self, data = None, next_node = None, previous_node = None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
    def get_previous(self):
        return self.previous_node
    def set_previous(self, new_next):
        self.previous_node = new_next

class DoublyLinkedList(MyList):
    def __init__(self, head=None):
        self.head = None
        self.node_count = 0

    def len(self):
        return self.node_count
    
    def getitem(self, j):
        if (self.node_count > j):
            cur = self.head
            for i in range(j):
                cur = cur.next_node
            return cur.data
        raise ValueError('value not in list')

    def setitem(self, val, j):
        if (self.node_count > j):
            cur = self.head
            for i in range(j):
                cur = cur.next_node
            cur.data = val
            return
        raise ValueError('index is out of bound')

    def insertItem(self, item, j=0):
        N_node = Node(item)
        if j == 0:
            if self.head is None:
                self.head = N_node
                self.node_count += 1
                return
            else:
                self.head.previous_node = N_node
                N_node.next_node = self.head
                self.head = N_node
                self.node_count += 1
                return
        elif j < self.node_count - 1:
            cur = self.head
            for i in range(j - 1):
                cur = cur.next_node
            temp = cur.next_node
            cur.set_next(N_node)
            N_node.set_previous(cur)
            N_node.set_next(temp)
            temp.set_previous(N_node)
            self.node_count += 1
        elif j == self.node_count-1:
            cur = self.head
            for i in range(j - 1):
                cur = cur.next_node
            cur.next_node = N_node
            N_node.previous_node = cur
            self.node_count += 1

    def removeItem(self, j=0):
        if j == 0:
            if self.node_count == 1:
                N_node = self.head.previous_node
                N_node = None
                self.head = N_node
                print("No data")
                self.node_count -= 1
            else:
                self.head = self.head.next_node
                self.head.previous_node = None
                self.node_count -= 1

        elif j > 0 and j < self.node_count-1:
            cur = self.head
            for i in range(j):
                cur = cur.next_node
            cur.previous_node.set_next(cur.next_node)
            cur.next_node.set_previous(cur.previous_node)
            self.node_count -= 1

        elif j == self.node_count-1:
            cur = self.head
            for i in range(j):
                cur = cur.next_node
            cur.previous_node.next_node = None
            self.node_count -= 1

        elif j >= self.node_count:
            raise ValueError('index out of bound')

    def printMyList(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end=' ')
            ptr = ptr.next_node
        print(" ")






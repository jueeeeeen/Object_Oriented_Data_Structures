class Node:
        def __init__(self, data, prev = None, next = None):
            self.data = data
            self.prev = None
            self.next = None
        def __str__(self):
            return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            p.prev = t
        self.size += 1

    def addHead(self, data):
        p = Node(data)
        self.head.prev = p
        p.next = self.head
        self.head = p
        self.size += 1
    
    def insert(self, index, data):
        p = Node(data)
        q = self.head
        while self.size*-1 <= index < 0:
            index += self.size
        if index < self.size*-1:
            index = 0
        count = 0
        while q != self.tail:
            if count == index:
                p.next = q.next

    def search(self, data):
        pass

    def index(self, data):
        pass

    def size(self):
        return self.size
    
    def pop(self, index):
        if self.head == None: return self.head.data
        if self.head.next == self.tail:
            data = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return data
        else:
            p = self.head
            while p.next.next != self.tail:
                p = p.next
            data = p.next.data
            p.next = p.next.next
            self.tail.prev = p
            self.size -= 1
            return data

    def insertAfter(self, i, data):
        p = Node(data)
        q = self.head
        count = 0
        while q != None:
            if count == i:
                p.next = q.next
                q.next = p
                return
            q = q.next
            count += 1

    def deleteAfter(self, i):
        q = self.head
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                p = None
                return
            q = q.next
            count += 1
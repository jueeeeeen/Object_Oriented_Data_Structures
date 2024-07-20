class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
        self.size = 0
    def __str__(self):
        return str(self.data)

class list:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        s = ""
        p = self.head
        while p != None:
            s += str(p.data)
            if p.next != None:
                s += " "
            p = p.next
        return s
    
    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def add_head(self, data):
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def remove_head(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def remove_tail(self):
        if self.head == None: return self.head.data
        if self.head.next == None:
            data = self.head
            self.head = None
            self.size -= 1
            return data
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            data = p.next.data
            p.next = p.next.next
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
                self.size += 1
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
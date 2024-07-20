class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.data) + " "
        while cur.prev != None:
            s += str(cur.prev.data) + " "
            cur = cur.prev
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            p.prev = t
            self.tail = p
            
    def addHead(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
            self.tail = p
            return
        self.head.prev = p
        p.next = self.head
        self.head = p
    
    def insert(self, index, data):
        p = Node(data)
        q = self.head
        if self.isEmpty():
            self.head = p
            self.tail = p
            return
        if index >= self.size():
            self.append(data)
            return
        if index < self.size()*-1:
            self.addHead(data)
            return
        elif index >= self.size():
            index = self.size()
            print(index)
            
        while index < 0:
            index += self.size()
        
        count = 0
        while q != None:
            if count == index:
                p.next = q
                p.prev = q.prev
                q.prev = p
                p.prev.next = p
                return
            q = q.next
            count += 1
        
        

    def search(self, data):
        q = self.head
        while q != None:
            if q.data == data:
                return "Found"
            q = q.next
        return "Not Found"

    def index(self, data):
        q = self.head
        index = 0
        while q != None:
            if q.data == data:
                return index
            q = q.next
            index += 1
        return -1

    def size(self):
        if self.head == None: return 0
        size = 0
        p = self.head
        while p != None:
            size += 1
            p = p.next
        return size
    
    def pop(self, index):
        if index > self.size() - 1 or self.head == None: return "Out of Range"
        if self.head.next == None and index == 0:
            self.head = None
            return "Success"
        t = self.head
        count = 0
        while t != self.tail:
            if count == index:
                t.prev.next = t.next
                t.next.prev = t.prev
                t = None
                return "Success"
            count += 1
            t = t.next

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
            

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)

class list:
    def __init__(self):
        self.header = Node()
        self.size = 1

    def __str__(self):
        if self.size == 1:
            return "List is empty"
        s = ""
        p = self.header.next
        s += "link list : "
        while p != None:
            if p.next == None:
                s += str(p.data)
            else:
                s += str(p.data) + "->"
            p = p.next
        return s
    
    def isEmpty(self):
        return self.size == 1

    def append(self, data):
        p = Node(data)
        t = self.header
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
        if self.header == None: return
        if self.header.next == None:
            p = self.header
            self.header = None
        else:
            p = self.head
            self.header = self.header.next
        self.size -= 1
        return p.data
    
    def remove_tail(self):
        if self.header.next == None:
            self.size -= 1
            return
        p = self.header.next
        while p.next.next != None:
            p = p.next
        p.next = p.next.next
        self.size -= 1

    def deleteAfter(self, i):
        q = self.header
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                p = None
                return
            q = q.next
            count += 1
            
    def insert(self, index, data):
        p = Node(data)
        q = self.header
        count = 0
        while q != None:
            if count == index:
                p.next = q.next
                q.next = p
                self.size += 1
                return
            q = q.next
            count += 1

insert_list = input("Enter Input : ").split(",")
datas = [int(x) for x in insert_list.pop(0).split(" ") if x.isnumeric()]

linked_list = list()
for data in datas:
    linked_list.append(data)
print(linked_list)

for insert in insert_list:
    index, data = [int(x) for x in insert.split(":")]
    if (index >= 0 and index <= linked_list.size):
        print(f"index = {index} and data = {data}")
    else:
        print("Data cannot be added")
    linked_list.insert(index, data)
    print(linked_list)
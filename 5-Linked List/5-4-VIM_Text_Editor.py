class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

        def __str__(self):
            return str(self.data)
                
class VIMLinkedList:
    def __init__(self):
        self.cursor = Node("|")
        self.head = self.cursor
        self.tail = self.cursor

    
    def __str__(self):
        cur, s = self.head, str(self.head) + " "
        while cur.next != None:
            s += str(cur.next) + " "
            cur = cur.next
        return s

    def insert_at_cursor(self, word):
        p = Node(word)
        t = self.cursor
        p.next = t
        p.prev = t.prev
        if t.prev != None:
            t.prev.next = p
        t.prev = p
        if p.prev == None:
            self.head = p
        return
    
    def move_left(self):
        c = self.cursor
        if c.prev != None:
            next = c.next
            prev = c.prev
            c.next = prev
            c.prev = prev.prev
            prev.next = next
            prev.prev = c
            if c.prev == None:
                self.head = c
            if prev.next == None:
                self.tail = prev
            if next != None:
                next.prev = prev
            if c.prev != None:
                c.prev.next = c
                
    def move_right(self):
        c = self.cursor
        if c.next != None:
            next = c.next
            prev = c.prev
            c.prev = next
            c.next = next.next
            next.prev = prev
            next.next = c
            if next.prev == None:
                self.head = next
            if c.next == None:
                self.tail = c
            if prev != None:
                prev.next = next
            if c.next != None:
                c.next.prev = c
            
    def delete_left(self):
        c = self.cursor
        if c.prev == None:
            return
        c.prev = c.prev.prev
        if c.prev == None:
            self.head = c
        if c.prev != None:
            c.prev.next = c
    
    def delete_right(self):
        c = self.cursor
        if c.next == None:
            return
        c.next = c.next.next
        if c.next == None:
            self.tail = c
        if c.next != None:
            c.next.prev = c
                
input = input("Enter Input : ").split(",")

linked_list = VIMLinkedList()

for x in input:
    if x[0] == "I":
        linked_list.insert_at_cursor(x[2:])
    elif x == "L":
        linked_list.move_left()
    elif x == "R":
        linked_list.move_right()
    elif x == "B":
        linked_list.delete_left()
    elif x == "D":
        linked_list.delete_right()
print(linked_list)
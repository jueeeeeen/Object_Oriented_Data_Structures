from collections import deque

class Queue:
    def __init__(self) :
        self.items = deque()
            
    def __str__(self):
        s = 'Queue of '+ str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s

    def isEmpty(self) :
        return self.items == []

    def enQueue(self,data) :
        self.items.append(data)

    def deQueue(self) :
        return self.items.popleft()

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]
    
# อาจารย์ให้ลอง
list = [5, 7, 6, 3, 8, 4]

q = Queue()

for num in list:
    q.enQueue(num)
    print(q)
    
for i in range(q.size()):
    print(q.deQueue())

print(q)
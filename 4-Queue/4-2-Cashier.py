class Queue:
    def __init__(self,list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def __str__(self):
        return str(self.items)

    def isEmpty(self) :
        return self.items == []

    def enQueue(self,data) :
        self.items.append(data)

    def deQueue(self) :
        return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]

def cashier_queing(list):
    main_q = Queue(list)
    cashier1 = Queue()
    cashier2 = Queue()
    
    minute = 0
    minute2 = 0
        
    while not main_q.isEmpty():
        if not cashier1.isEmpty() and minute % 3 == 0:
            cashier1.deQueue()
        if not cashier2.isEmpty() and minute2 % 2 == 0:
            cashier2.deQueue()
            
        if cashier1.size() < 5:
            cashier1.enQueue(main_q.deQueue())
        elif cashier2.size() < 5:
            cashier2.enQueue(main_q.deQueue())
            
        minute += 1
        if not cashier2.isEmpty():
            minute2 += 1
        
        print(f"{minute} {main_q} {cashier1} {cashier2}")
                
list = list(input("Enter people : "))

cashier_queing(list)



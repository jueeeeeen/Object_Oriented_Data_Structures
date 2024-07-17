class Stack:
    def __init__(self, items= None):
        if items:
            self.items = items
        else:
            self.items = []
            
    def __str__(self):
        return str(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        
    def size(self) :
        return len(self.items)
    
def parkingManager(m, s, o, n):
    vilA = Stack([int(x) for x in s.split(",") if int(x) != 0])
    vilB = Stack()
    finished = 0
    if o == "arrive":
        if vilA.size() == m:
            print(f"car {n} cannot arrive : Soi Full")
        else:
            while not vilA.isEmpty():
                if vilA.peek() == n:
                    print(f"car {n} already in soi")
                    finished = 1
                    break
                vilB.push(vilA.pop())
            while not vilB.isEmpty():
                vilA.push(vilB.pop())
            if not finished:
                vilA.push(n)
                print(f"car {n} arrive! : Add Car {n}")
    elif o == "depart":
        if vilA.isEmpty():
            print(f"car {n} cannot depart : Soi Empty")
        else:
            while not vilA.isEmpty():
                if vilA.peek() == n:
                    print(f"car {vilA.pop()} depart ! : Car {n} was remove")
                    finished = 1
                    break
                vilB.push(vilA.pop())
            else:
                if not finished:
                    print(f"car {n} cannot depart : Dont Have Car {n}")
            while not vilB.isEmpty():
                vilA.push(vilB.pop())
    print(vilA)
                
            
            

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()


m,n = int(m),int(n)

parkingManager(m, s, o, n)
### Enter Your Code Here ###
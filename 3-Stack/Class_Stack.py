class Stack :
    def __init__(self,list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s

    def isEmpty(self) :
        return self.items == []

    def push(self,data) :
        self.items.append(data)

    def pop(self) :
        return self.items.pop()

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]
class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return "Empty"
        s = ""
        s += f"({self.head})"
        p = self.head.next
        if p == None:
            s += "->Empty"
        while p != None:
            s += "->" + str(p)
            p = p.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
            return
        t = self.head
        while t.next != None:
            t = t.next
        t.next = p

    def remove_tail(self):
        t = self.head
        while t.next.next != None:
            t = t.next
        p = t.next
        t.next = t.next.next
        t.next = None
        return p.data
    
    def sum_of_weights(self):
        t = self.head
        weight = 0
        while t != None:
            weight += t.data
            t = t.next
        return weight
    
    def peek_last_snake(self):
        t = self.head
        while t.next != None:
            t = t.next
        return t.data
        
    def play(self, weight):
        falls = []
        if self.sum_of_weights() >= weight:
            return "Play success!->[]"
        
        t = self.head.next
        while t != None:
            if t.data != 0 and weight % t.data == 0:
                break
            t = t.next
        else:
            t = self.head
            while t.next.next != None:
                t = t.next
            
            p = t.next
            if self.head.next.next != None:
                p.next = self.head.next
                t.next = self.head
            else:
                p.next = self.head
                
            self.head.next = None
            self.head = p
            return "Play success!->[]"
        
        while (self.peek_last_snake() != 0 and weight % self.peek_last_snake() != 0) or self.peek_last_snake() == 0:
            falls.append(self.remove_tail())
        
        return "Play success!->" + str(falls[::-1])
    
    def fly(self, weight):
        self.append(weight)
        return "Steal success!->" + str(weight)
    
    def swap(self):
        t = self.head
        while t.next != None:
            p = t.next
            q = t.next.next
            if t.next.next != None:
                p.next = q.next
                q.next = p
            t.next = q
            t = p
        return "Swap success!"
            
    
    def shake(self):
        falls = []
        t = self.head
        while t != None and t.next != None:
            if t.next.data > self.head.data:
                falls.append(t.next.data)
                p = t.next
                t.next = p.next
            else:
                t = t.next
        return "Shake success!->" + str(falls)
    
    def is_Mom_dead(self):
        return self.head == None or self.head.next == None

def snake_game(snakes, commands):
    snake_list = LinkedList()
    if snakes != None:    
        for snake in snakes:
            snake_list.append(int(snake))
        
    print(snake_list)
        
    for command in commands:
        if snake_list.is_Mom_dead():
            print("Mom is dead")
            break
        if command[0] == "D":
            print(snake_list.play(int(command[2:])))
        elif command[0] == "F":
            print(snake_list.fly(int(command[2:])))
        elif command == "SW":
            print(snake_list.swap())
        elif command == "SH":
            print(snake_list.shake())
        print(snake_list)
        print("------------------------------")
    else:
        if snake_list.is_Mom_dead():
            print("Mom is dead")

while 1:
    snakes, commands = input("Snake Game : ").split("/")
    if snakes != "":
        snakes = snakes.split(" ")
    else:
        snakes = None
    commands = commands.split(",")
    snake_game(snakes, commands)
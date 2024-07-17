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

def decoded(c, num):
    x = ord(c)+num
    if "A" <= c <= "Z":
        if x < 65:
            return chr(x+26)
        elif x > 90:
            return chr(x-26)
    elif "a" <= c <= "z":
        if x < 97:
            return chr(x+26)
        elif x > 122:
            return chr(x-26)
    return chr(x)
        
def processmsg(q1, q2, op):
    for i in range(q1.size()):
        q2.enQueue(q2.deQueue())
        q1.enQueue(decoded(q1.deQueue(), op*int(q2.peek())))
    for j in range(q2.size() - (q1.size() % q2.size())):
        q2.enQueue(q2.deQueue())
    return q1
        
def encodemsg(q1, q2):
    return processmsg(q1, q2, 1)

def decodemsg(q1, q2):
    return processmsg(q1, q2, -1)
        
string, number = input("Enter String and Code : ").split(",")
string = [x for x in string if x != " "]
number = [int(x) for x in number]

q1 = Queue(string)

q2 = Queue(number)

print(f"Encode message is :  {encodemsg(q1, q2)}")

print(f"Decode message is :  {decodemsg(q1, q2)}")
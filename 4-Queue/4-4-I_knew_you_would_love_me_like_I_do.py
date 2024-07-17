class Queue:
    def __init__(self,list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def __str__(self):
        return ", ".join(self.items)

    def isEmpty(self) :
        return self.items == []

    def enQueue(self, data) :
        self.items.append(data)

    def deQueue(self) :
        return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]

convert = {"act":{"0":"Eat", "1":"Game", "2":"Learn", "3":"Movie"}, "place":{"0":"Res.", "1":"ClassR.", "2":"SuperM.", "3":"Home"}}

queues = input("Enter Input : ").split(",")
score = 0

myqueue = Queue()
yourqueue = Queue()

for queue in queues:
    mine, yours = queue.split(" ")
    myqueue.enQueue(mine)
    yourqueue.enQueue(yours)

print(f"My   Queue = {myqueue}")
print(f"Your Queue = {yourqueue}")

for i in range(myqueue.size()):
    mine = myqueue.deQueue()
    yours = yourqueue.deQueue()
    if mine[0] == yours[0] and mine[2] != yours[2]:
        score += 1
    elif mine[0] != yours[0] and mine[2] == yours[2]:
        score += 2
    elif mine == yours:
        score += 4
    else:
        score -= 5

    myqueue.enQueue(f"{convert['act'][mine[0]]}:{convert['place'][mine[2]]}")
    yourqueue.enQueue(f"{convert['act'][yours[0]]}:{convert['place'][yours[2]]}")

print(f"My   Activity:Location = {myqueue}")
print(f"Your Activity:Location = {yourqueue}")

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif 0 < score < 7:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")
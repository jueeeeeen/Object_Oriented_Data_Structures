class Queue:
    def __init__(self,list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def __str__(self):
        return 'Queue: ' + str(self.items)

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
    
def search_portal(width, height, map = []):
    q = Queue()
    visited = []
    output = ""
    
    if len(map) != height or len(map[0]) != width:
        return "Invalid map input."
    
    for Ymap in map:
        if len(Ymap) != width:
            return "Invalid map input."
    
    for y in range(height):
        for x in range(width):
            if "F" == map[y][x]:
                q.enQueue((x, y))
                visited.append((x, y))
                output += str(q) + "\n"
                break
        else:
            continue
        break
    else:
        return "Invalid map input."
    
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while not q.isEmpty():
        x, y = q.deQueue()
        for i, j in dir:
            Px, Py = x+i, y+j
            if not (Px < 0 or Px > width - 1 or Py < 0 or Py > height - 1) and (Px, Py) not in visited:
                if map[Py][Px] == "_":
                    q.enQueue((Px, Py))
                    visited.append((Px, Py))
                elif map[Py][Px] == "O":
                    output += "Found the exit portal."
                    break
        else:
            if not q.isEmpty():
                output += str(q) + "\n"
            continue
        break
    else:
        output += "Cannot reach the exit portal."
    return output
    
width, height, map = input("Enter width, height, and room: ").split(" ")
width = int(width)
height = int(height)
map = map.split(",")
print(search_portal(width, height, map))
actions = input("Enter Input : ").split(",")
queue = []

for action in actions:
    if action[0] == "E":
        queue.append((action[2:]))
        print(len(queue))
    elif action == "D":
        if queue == []:
            print("-1")
        else:
            print(f"{queue[0]} 0")
            del queue[0]
if queue:
    print(' '.join(queue))
else:
    print("Empty")
print("*** TorKham HanSaa ***")
actions = (input("Enter Input : ")).split(",")
words = []
for action in actions:
    if action == "R":
        words = []
        print("game restarted")
    elif action == "X":
        break
    elif action[:2] == "P ":
        word = action[2:]
        if words == [] or word[:2].lower() == words[-1][-2:].lower():
            words.append(word)
            print("'"+ words[-1]+"' ->" ,words)
        else:
            print("'"+ word +"' -> game over")
            break
    else:
        print("'"+ action +"'", "is Invalid Input !!!")
        break
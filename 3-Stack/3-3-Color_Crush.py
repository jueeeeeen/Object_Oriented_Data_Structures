check = 1
colors = input("Enter Input : ").split(" ")
combo = 1

while check == 1:
    temp = []
    stack = []
    for color in colors:
        if len(stack) < 3 and (stack == [] or stack[-1] == color):
            stack.append(color)
        else:
            if len(stack) != 3:
                while stack:
                    temp.append(stack.pop())
                stack.append(color)
            else:
                temp.append(color)
    if len(stack) == 3:
        combo += 1
        colors = temp
        check = 1
    else:
        check = 0
print(len(colors))
if not colors: print("Empty", end="")
while colors:
    print(colors.pop(), end="")

if combo-1 > 1:
    print(f"\nCombo : {combo-1} ! ! !")